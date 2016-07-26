from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

User = get_user_model()

class AccountLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError("This username does not exist")

        if not user.check_password(password):
            raise forms.ValidationError("This password not confere")

        if not user.is_active:
            raise forms.ValidationError("This username does not active")
        return super(AccountLoginForm, self).clean(*args, **kwargs)


class RegisterAccountForm(forms.ModelForm):
    email = forms.EmailField(label='Informe seu e-mail')
    email2 = forms.EmailField(label='Confirme seu e-mail')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError('Os e-mails são diferentes')

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("E-mail já registrado")

        return super(RegisterAccountForm, self).clean(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError('Os e-mails são diferentes')

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("E-mail já registrado")

        return email