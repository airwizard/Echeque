# djangotemplates/example/views.py
from django.conf import settings

from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView # Import TemplateView

from account.models import Friends, Customer
from transaction.models import Transaction
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as au_login
from django.contrib.auth import logout as au_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as auth_login
from django.contrib.auth.backends import ModelBackend
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from Echeque.config import public_web3, public_psn, banks

# from django.contrib.auth import  auth_login
from django.core.urlresolvers import reverse
import json


@csrf_exempt
@login_required
def index(request):
    if request.user.is_authenticated:
        print "already login"
    else:
        print "not login yet"
    if request.method == 'GET':
        return redirect('balance')


@csrf_exempt
def regist(request):
    if request.method == 'GET':
        return render(request, 'regist.html')
    if request.method == 'POST':
        try:
            username = str(request.POST.get('username'))
            password = str(request.POST.get('password'))
            repassword = str(request.POST.get('repassword'))
            email = str(request.POST.get('email'))
        except Exception, e:
            print str(e)
            return HttpResponse(json.dumps({'message': "Input error."}), content_type="application/json")

        if len(User.objects.filter(email=email)) > 0:
            return HttpResponse(json.dumps({'message': "Email exists."}), content_type="application/json")

        if repassword != password:
            return HttpResponse(json.dumps({'message': "Passwords do not match."}), content_type="application/json")


        try:
            user_obj = User.objects.create_user(username=username, password=password, email=email)
            # user_obj = User.objects.create(username=username, password=password, email=email, eth_addr=address)
            # user_obj.save()
            user_obj.save()
            Customer.objects.create(user_id=user_obj.id, eth_addr="")
            return HttpResponse(json.dumps({'message': "success"}), content_type="application/json")
        except Exception, e:
            print str(e)
            return HttpResponse(json.dumps({'message': str(e)}), content_type="application/json")


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        try:
            email = str(request.POST.get('email'))
            password = str(request.POST.get('password'))
            user = User.objects.get(email=email)
            # customer = Customer.objects.get(user_id=user.id)
        except Exception:
            HttpResponse(json.dumps({'message': "User not exist."}), content_type="application/json")

        auth_user = authenticate(username=user.username, password=password)
        if user.check_password(password):
            au_login(request, auth_user)
            return HttpResponse(json.dumps({'message': "success",
                                            'user_id': user.id,
                                            'username': user.username}),
                                content_type="application/json")
        else:
            return HttpResponse(json.dumps({'message': "Wrong password."}), content_type="application/json")


@csrf_exempt
@login_required
def create_account(request):
    if request.method == 'POST':
        try:
            cus_obj = Customer.objects.get(user_id=request.user.id)
            account_pass = str(request.POST.get('password'))
        except Exception, e:
            print str(e)
            return HttpResponse(json.dumps({'message': 'Error parameter.'}),
                                content_type="application/json")

        try:
            from_addr = cus_obj
            if not (from_addr is None or from_addr==""):
                return redirect('/transaction/balance/')


            address = public_psn.newAccount(account_pass)
            if not public_web3.isAddress(address):
                return HttpResponse(json.dumps({'message': "Cannot create Ethereum account."}),
                                    content_type="application/json")
            cus_obj.eth_addr = address
            cus_obj.save()

            public_psn.unlockAccount(banks['HSBC']['address'], banks['HSBC']['password'], 1000)

            trans_hash = public_web3.eth.sendTransaction(
                {'from': banks['HSBC']['address'], 'to': address, 'value': public_web3.toWei(100,'Ether'),
                 'gasPrice': 100000000, 'gas': 21000})

            return HttpResponse(json.dumps({'message': 'success',
                                            'address': address}),
                                content_type="application/json")
        except Exception, e:
            print str(e)
            return HttpResponse(json.dumps({'message': str(e)}), content_type="application/json")

@login_required
@csrf_exempt
def setting(request):
    if request.method == 'GET':
        return render(request, 'setting.html')

    if request.method == 'POST':
        try:
            old_pwd = str(request.POST.get('old_pwd'))
            new_pwd = str(request.POST.get('new_pwd'))
            repeat_pwd = str(request.POST.get('repeat_pwd'))

        except Exception:
            return HttpResponse(json.dumps({'message': "Error data."}), content_type="application/json")

        if new_pwd != repeat_pwd:
            return HttpResponse(json.dumps({'message': "Passwords do not match."}), content_type="application/json")

        if request.user.check_password(old_pwd):
            request.user.set_password(new_pwd)

            return HttpResponse(json.dumps({'message': "success"}),
                                content_type="application/json")
        else:
            return HttpResponse(json.dumps({'message': "Wrong old password."}), content_type="application/json")


@login_required
@csrf_exempt
def address_book(request):
    if request.method == 'GET':
        return render(request, 'address.html')

    if request.method == 'POST':
        try:
            frnd_list = Friends.objects.filter(user_id=request.user.id)

            if len(frnd_list) == 0:
                return HttpResponse(json.dumps({'message': "success", 'data':json.dumps([])}),
                                    content_type="application/json")

            data = []
            for frnd in frnd_list:
                data.append([frnd.friend_name, frnd.friend_email, frnd.friend_addr])

            return HttpResponse(json.dumps({'message': "success", 'data':json.dumps(data)}),
                                content_type="application/json")
        except Exception, e:
            return HttpResponse(json.dumps({'message': str(e)}), content_type="application/json")



@login_required
@csrf_exempt
def logout(request):
    au_logout(request)
    return redirect('login')


@csrf_exempt
def trans_list(request):
    if request.method == 'GET':
        return render(request, 'trans_list.html')
    if request.method == 'POST':
        try:
            data = []
            trans_list = Transaction.objects.filter()
            for t in trans_list:
                if public_web3.eth.getTransaction(t.trans_hash) is None:
                    t.delete()
                if t.trans_status is False and public_web3.eth.getTransactionReceipt(t.trans_hash) is not None:
                    t.trans_status = True
                    t.save()
                data.append([t.trans_hash,t.trans_type,t.trans_from,t.trans_status])
            return HttpResponse(json.dumps({'message': 'success', 'data':data}),
                                content_type="application/json")
        except Exception,e:
            return HttpResponse(json.dumps({'message': str(e)}),
                                content_type="application/json")
