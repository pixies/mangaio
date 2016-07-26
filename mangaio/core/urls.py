from django.conf.urls import patterns, url
from mangaio.core.views import home, contact

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contato/', contact, name='contact'),
]
