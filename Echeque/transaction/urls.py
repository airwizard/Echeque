from django.conf.urls import url
from transaction import views



urlpatterns = [

    # url(r'$', views.login, name='login'),
    url(r'^balance/$', views.balance, name='balance'),
    url(r'^address/$', views.address, name='address'),
    url(r'^deposit/$', views.deposit, name='deposit'),
    url(r'^issue_echeque/$', views.issue_echeque, name='issue_echeque'),
    url(r'^transfer_echeque/$', views.transfer_echeque, name='transfer_echeque'),
    # url(r'^echeque_list/$', views.echeque_list, name='echeque_list'),
    url(r'^echeque/$', views.echeque, name='echeque'),
    url(r'^cash_echeque/$', views.cash_echeque, name='cash_echeque'),
    url(r'^get_echeque_amount/$', views.get_echeque_amount, name='get_echeque_amount'),
    url(r'^unlock_account/$', views.unlock_account, name='unlock_account'),

]
