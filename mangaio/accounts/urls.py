from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^entrar/$', 'django.contrib.auth.views.login',
    {'template_name': 'accounts/login.html'}, name='login'),

    url(r'^cadastre-se/$', 'mangaio.accounts.views.register', name='register'),

    #url(r'^sair/$', 'django.contrib.auth.views.logout',
    #{'next_page': 'core:home'}, name='logout'),

)