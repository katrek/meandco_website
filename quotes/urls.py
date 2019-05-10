from django.conf.urls import url
from .views import QuoteList

from . import views

urlpatterns = [
    url(r'^$', views.quote_req, name='quote-request'),
    url(r'show$', QuoteList.as_view(), name='show-quotes'),
]