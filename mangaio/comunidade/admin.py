from django.contrib import admin
from mangaio.comunidade.models import Usuario,UserProfile,Endereco,RedeSocial

# Register your models here.
admin.site.register(Usuario)
admin.site.register(UserProfile)
admin.site.register(Endereco)
admin.site.register(RedeSocial)
