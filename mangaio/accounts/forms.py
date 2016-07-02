from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):

    email - forms.EmailField(label='E-mail')

    if User.objects.filter(email=email).exists():
        raise forms.ValidationError(
            ('O e-mail, %(value)s, ja esta cadastrado'),
            params={'value':email}
        )
    return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def __unicode__(self):
        return self.email

