from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

from account.models import Customer
from django.contrib.auth.models import User
from transaction.models import Transaction
from account.models import Friends
from Echeque.config import public_web3, public_psn, contract, banks


from django.contrib.auth.decorators import login_required
from Echeque.settings import BASE_DIR
from django.core.urlresolvers import reverse
# from django.template import RequestContext
from django.template.loader import render_to_string

from django.core.mail import EmailMessage
import eth_abi
import json
import os
import web3
import time
import random
from collections import OrderedDict
import Tkinter
from reportlab.pdfgen import canvas
from PIL import Image
from num2words import num2words
import eth_rpc_client


@csrf_exempt
@login_required
def balance(request):
    if request.method == 'GET':
        try:
            cus_obj = Customer.objects.get(user_id=request.user.id)
            print cus_obj
            from_addr = cus_obj.eth_addr
            if from_addr is not None and from_addr != "":
                balance = contract.call().getBalance(from_addr)
                balance = '%.2f' % (float(balance) / 100)
                own_echeque = contract.call().getEchequesByAccount(from_addr)
                print own_echeque
                echeque_list = []
                for e in own_echeque:
                    amount = contract.call().getEchequeAmount(e)
                    drawer = contract.call().getEchequeDrawer(e)
                    payee = contract.call().getEchequePayee(e)
                    echeque_list.append({'echeque_no': e,
                                         'amount': '%.2f' % (float(amount) / 100),
                                         'drawer': drawer,
                                         'payee': payee})

                return render(request, 'balance.html', {'from_addr':from_addr,'balance':balance,'echeque_list':echeque_list, 'message':'success'})
            else:
                return render(request, 'create_account.html')
        except Exception, e:
            print str(e)
            return render(request, 'balance.html', {'echeque_list':[], 'message': str(e)})


        # try:
        #
        #     print address
        #     if not public_web3.isAddress(address):
        #         return HttpResponse(json.dumps({'message': "Cannot create Ethereum account."}),
        #                             content_type="application/json")
        # except Exception, e:
        #     print str(e) + '1111'
        #     return HttpResponse(json.dumps({'message': "Cannot connect to Ethereum network."}),
        #                         content_type="application/json")


    # if request.method == 'POST':
    #     try:
    #         cus_obj = Customer.objects.get(user_id=request.user.id)
    #         address = cus_obj.eth_addr
    #         if address is None:
    #             return  HttpResponse(json.dumps({'message': 'Please create account.'}),
    #                             content_type="application/json")
    #
    #         balance = float(contract.call().getBalance(address)) / 100
    #
    #         return HttpResponse(json.dumps({'message':'success',
    #                                         'address': address,
    #                                         'balance': balance}),
    #                             content_type="application/json")
    #     except Exception,e:
    #         return HttpResponse(json.dumps({'message': str(e)}),
    #                             content_type="application/json")




@csrf_exempt
@login_required
def deposit(request):
    if request.method == 'GET':
        return render(request, 'deposit.html')
    if request.method == 'POST':
        try:
            bankName = request.POST.get('bankName')
            amount = float(request.POST.get('amount'))

            if int(amount*100) != amount*100:
                return HttpResponse(json.dumps({'message': 'Please input a number with at most two decimals.'}),
                                    content_type="application/json")
            else:
                amount = int(amount*100)

            bank_addr = banks['HSBC']['address']
            bank_pwd = banks['HSBC']['password']

            cus_obj = Customer.objects.get(user_id=request.user.id)
            address = cus_obj.eth_addr
            public_psn.unlockAccount(bank_addr, bank_pwd, 1000)
            trans_hash = contract.transact({'from':bank_addr}).deposit(address, amount)

            #echeque_no = time.strftime('%Y%m%d%H%M%S')+ str(random.randint(0, 9))
            #echeque_no = int(echeque_no)

            Transaction.objects.create(trans_hash=trans_hash,trans_type='deposit', trans_from=bank_addr,trans_status=False)

            return HttpResponse(json.dumps({'message':'success'}),
                                content_type="application/json")
        except Exception,e:
            return HttpResponse(json.dumps({'message': str(e)}),
                                content_type="application/json")


@csrf_exempt
@login_required
def issue_echeque(request):
    if request.method == 'GET':
        try:
            cus_obj = Customer.objects.get(user_id=request.user.id)
            from_addr = cus_obj.eth_addr

            frnd_list = Friends.objects.filter(user_id=request.user.id)
            to_list = []
            for frnd in frnd_list:
                to_list.append({'email': frnd.friend_email, 'name': frnd.friend_name})

            return render(request, 'issue_echeque.html', {'from_addr':from_addr, 'to_list':to_list, 'message':'success'})
        except Exception, e:
            return render(request, 'issue_echeque.html',
                          {'from_addr': from_addr, 'to_list': [], 'message': str(e)})

    if request.method == 'POST':
        try:
            print request.POST
            from_addr = request.POST.get('from_addr')
            payee = str(request.POST.get('payee_name'))
            amount = float(request.POST.get('amount'))

            if int(amount*100) != amount*100:
                return HttpResponse(json.dumps({'message': 'Please input a number with at most two decimals.'}),
                                    content_type="application/json")
            else:
                amount = int(amount*100)

            balance = contract.call().getBalance(from_addr)
            if amount > balance:
                return HttpResponse(json.dumps({'message': 'Insufficient Balance.'}),
                                    content_type="application/json")

            cus_obj = Customer.objects.get(user_id=request.user.id)
            if not public_web3.isAddress(from_addr) or str(from_addr) != str(cus_obj.eth_addr) :
                return HttpResponse(json.dumps({'message': 'Invalid address.'}),
                                    content_type="application/json")

            echeque_no = time.strftime('%Y%m%d%H%M%S')+ str(random.randint(0, 9))
            echeque_no = int(echeque_no)

            if payee is None or payee == '':
                payee = 'None'
            trans_hash = contract.transact({'from':from_addr}).issueEcheque(str(request.user.username), payee, amount, echeque_no)

            if trans_hash is None:
                return HttpResponse(json.dumps({'message': 'Transaction error.'}),
                                    content_type="application/json")

            Transaction.objects.create(trans_hash=trans_hash,trans_type='issue_echeque', trans_from=from_addr,trans_status=False)

            return HttpResponse(json.dumps({'message':'success','echeque_no':echeque_no}),
                                content_type="application/json")
        except Exception,e:
            return HttpResponse(json.dumps({'message': str(e)}),
                                content_type="application/json")



@csrf_exempt
@login_required
def transfer_echeque(request):
    if request.method == 'GET':
        try:
            cus_obj = Customer.objects.get(user_id=request.user.id)
            from_addr = cus_obj.eth_addr
            own_echeque = contract.call().getEchequesByAccount(from_addr)
            print own_echeque
            if len(own_echeque) > 0:
                amount = float(contract.call().getEchequeAmount(own_echeque[0])) / 100
            else:
                amount = ''

            frnd_list = Friends.objects.filter(user_id=request.user.id)
            to_addr = []
            for frnd in frnd_list:
                to_addr.append({'email':frnd.friend_email, 'addr':frnd.friend_addr})

            return render(request, 'transfer_echeque.html', {'echeque_list':own_echeque, 'amount':amount, 'to_addr':to_addr, 'message':'success'})
        except Exception, e:
            print str(e)
            return render(request, 'transfer_echeque.html', {'message':str(e)})

    if request.method == 'POST':
        try:
            echeque_no = int(request.POST.get('echeque_no'))
            to_addr = request.POST.get('to_addr')

            if not public_web3.isAddress(to_addr):
                return HttpResponse(json.dumps({'message': 'Invalid address.'}),
                                    content_type="application/json")

            cus_obj = Customer.objects.get(user_id=request.user.id)
            from_addr = cus_obj.eth_addr

            if str(contract.call().traceEchequeOwner(echeque_no)[-1]) != str(from_addr) or not contract.call().ifEchequeValid(echeque_no):
                return HttpResponse(json.dumps({'message': 'You cannot operate this e-Cheque.'}),
                                    content_type="application/json")

            trans_hash = contract.transact({'from': from_addr}).transferEcheque(to_addr, echeque_no)

            if trans_hash is None:
                return HttpResponse(json.dumps({'message': 'Transaction error.'}),
                                    content_type="application/json")

            Transaction.objects.create(trans_hash=trans_hash, trans_type='transfer_echeque', trans_from=from_addr,
                                       trans_status=False)

            return HttpResponse(json.dumps({'message':'success'}),
                                content_type="application/json")
        except Exception,e:
            return HttpResponse(json.dumps({'message': str(e)}),
                                content_type="application/json")


@csrf_exempt
@login_required
def cash_echeque(request):
    if request.method == 'GET':
        try:
            cus_obj = Customer.objects.get(user_id=request.user.id)
            from_addr = cus_obj.eth_addr

            own_echeque = contract.call().getEchequesByAccount(from_addr)

            if len(own_echeque) > 0:
                amount = float(contract.call().getEchequeAmount(own_echeque[0])) / 100
            else:
                amount = ''

            return render(request, 'cash_echeque.html', {'echeque_list':own_echeque, 'amount':amount, 'success_flag':'true'})
        except Exception, e:
            print str(e)
            return render(request, 'cash_echeque.html', {'echeque_list': [], 'amount': '-1', 'success_flag':'false'})

    if request.method == 'POST':
        try:
            echeque_no = int(request.POST.get('echeque_no'))

            cus_obj = Customer.objects.get(user_id=request.user.id)
            from_addr = cus_obj.eth_addr

            if str(contract.call().traceEchequeOwner(echeque_no)[-1]) != str(from_addr) or not contract.call().ifEchequeValid(echeque_no):
                return HttpResponse(json.dumps({'message': 'You cannot operate this e-Cheque.'}),
                                    content_type="application/json")

            trans_hash = contract.transact({'from': from_addr}).cashEcheque(str(request.user.username),echeque_no)

            if trans_hash is None:
                return HttpResponse(json.dumps({'message': 'Transaction error.'}),
                                    content_type="application/json")

            Transaction.objects.create(trans_hash=trans_hash, trans_type='cash_echeque', trans_from=from_addr,
                                       trans_status=False)

            return HttpResponse(json.dumps({'message':'success'}),
                                content_type="application/json")
        except Exception,e:
            return HttpResponse(json.dumps({'message': str(e)}),
                                content_type="application/json")

@login_required
@csrf_exempt
def get_echeque_amount(request):
    if request.method == 'GET':
        try:
            echeque_no = int(request.GET.get('echeque_no'))
            amount = float(contract.call().getEchequeAmount(echeque_no)) / 100

            return HttpResponse(json.dumps({'message': 'success', 'amount':'%.2f'%amount}),
                                content_type="application/json")
        except Exception, e:
            return HttpResponse(json.dumps({'message': str(e)}),
                                content_type="application/json")


@login_required
@csrf_exempt
def address(request):
    # if request.method == 'GET':
    #     return render(request, 'address.html')

    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            frnd_obj = User.objects.get(email=email)
        except Exception, e:
            return HttpResponse(json.dumps({'message': 'Email does not exist.'}), content_type="application/json")

        try:
            cus_obj = Customer.objects.get(user_id=frnd_obj.id)
            address = cus_obj.eth_addr

            if address is None or address=="":
                return HttpResponse(json.dumps({'message': 'This user does not create a payment account'}), content_type="application/json")

            if len(Friends.objects.filter(user_id=request.user.id,friend_email=frnd_obj.email)):
                return HttpResponse(json.dumps({'message': 'This email is already in address book.'}), content_type="application/json")

            new_obj = Friends.objects.create(user_id=request.user.id, friend_name=frnd_obj.username, friend_email=frnd_obj.email, friend_addr=address)

            data = [new_obj.friend_name, new_obj.friend_email, new_obj.friend_addr]
            return HttpResponse(json.dumps({'message': "success", 'data': json.dumps(data)}),
                                content_type="application/json")
        except Exception, e:
            return HttpResponse(json.dumps({'message': str(e)}), content_type="application/json")


# @csrf_exempt
# @login_required
# def echeque_list(request):
#     if request.method == 'GET':
#         return render(request, 'echeque.html')
#     if request.method == 'POST':
#         try:
#             trans_list = Transaction.objects.filter(user_id=request.user.id)
#             trans_list = trans_list.order_by('-id')
#
#             data = []
#
#             for trans_obj in trans_list:
#                 trans_detail = public_web3.eth.getTransaction(trans_obj.trans_hash)
#                 if trans_detail is None:
#                     trans_obj.delete()
#                     continue
#                 amount = float(trans_detail['value']) / 1000000000000000000
#                 data.append([
#                     # trans_detail['from'],
#                     #          trans_detail['to'],
#                              trans_detail['hash'],
#                              str(trans_detail['blockNumber']),
#                              -amount if trans_obj.expend_flag else amount,
#                              True if trans_detail['blockNumber'] else False,
#                              trans_obj.echeque_no])
#
#             return HttpResponse(json.dumps({'message':'success', 'data': data}),
#                                 content_type="application/json")
#         except Exception,e:
#             return HttpResponse(json.dumps({'message': str(e)}),
#                                 content_type="application/json")


@csrf_exempt
@login_required
def echeque(request):
    if request.method == 'GET':
        echeque_no = request.GET.get('echeque_no')

        amount = contract.call().getEchequeAmount(int(echeque_no))
        drawer = contract.call().getEchequeDrawer(int(echeque_no))
        payee = contract.call().getEchequePayee(int(echeque_no))

        print amount,drawer,payee

        response = HttpResponse(content_type='application/pdf')


        response['Content-Disposition'] = 'attachment; filename="%s.pdf"' % echeque_no

        # Create the PDF object, using the response object as its "file."
        image_path = os.path.join(BASE_DIR, 'static/images/echeque.png')
        image = Image.open(image_path)

        p = canvas.Canvas(response, pagesize=image.size)

        p.drawImage(image_path, 0, 0, width=None,height=None)

        p.setFont("Helvetica", 24)

        if payee=='None':
            p.drawString(120, 230, 'Bearer')
        else:
            p.drawString(120, 230, payee)


        p.setFont("Helvetica", 24)
        #date = time.strftime("%b-%d-%Y")
        date = echeque_no[:4]+'-'+''+echeque_no[4:6]+'-'+echeque_no[6:8]
        p.drawString(590, 310, date)

        p.setFont("Helvetica", 24)
        value = float(amount) / 100
        # value = 123382244.31
        p.drawString(590, 240, "**%.2f**" % value)

        p.setFont("Helvetica", 24)
        p.drawString(580, 100, drawer)

        words = num2words(round(value,2)).title()+' Only**'
        if len(words) < 60:
            p.setFont("Helvetica", 24)
            p.drawString(200, 165, words)
        else:
            word_list = words.split(' ')
            num = 0
            first_line = ''
            second_line = ''
            for w in word_list:
                num = num + len(w)
                if num < 65:
                    first_line = first_line + w + ' '
                else:
                    second_line = second_line + w + ' '
            p.setFont("Helvetica", 20)
            p.drawString(180, 185, first_line)
            p.drawString(180, 165, second_line)

        p.setFont("Helvetica", 16)
        p.drawString(60, 40, "No: " + str(echeque_no))

        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()

        return response


@csrf_exempt
@login_required
def unlock_account(request):
    if request.method == 'POST':
        try:
            password = request.POST.get('password')
            cus_obj = Customer.objects.get(user_id=request.user.id)
            from_addr = cus_obj.eth_addr
            public_psn.unlockAccount(from_addr, password, 100000)
            return HttpResponse(json.dumps({'message': 'success'}),
                                content_type="application/json")
        except Exception, e:
            print str(e)
            return HttpResponse(json.dumps({'message': 'Cannot unlock account. Please try it again.'}),
                                content_type="application/json")


