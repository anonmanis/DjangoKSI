from django import forms
from captcha.fields import CaptchaField
from ujian_aplikasi_1174043.models import User


class NewUserForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = '__all__'