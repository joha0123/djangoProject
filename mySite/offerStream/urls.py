from django.conf.urls import url

from . import views

app_name = 'offerStream'
urlpatterns = [
	url(r'^all$', views.allOffers, name='allOffers')
]
