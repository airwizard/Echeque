from django.conf.urls import url
from account import views



urlpatterns = [
    # url(r'^home/$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    # url(r'^about/$', views.AboutPageView.as_view(), name='about'),

    url(r'^index/$', views.index, name='index'),

    # url(r'$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^setting/$', views.setting, name='setting'),
    url(r'^address_book/$', views.address_book, name='address_book'),
    url(r'^create_account/$', views.create_account, name='create_account'),
    url(r'^trans_list/$', views.trans_list, name='trans_list'),
]
