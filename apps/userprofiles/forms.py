# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, Submit, HTML, Div, MultiField
from crispy_forms.bootstrap import FormActions, PrependedText


class ProfileForm(UserCreationForm):

    user_phone = forms.CharField(max_length=12)
    avatar = forms.ImageField()
    calification = forms.IntegerField(initial=0)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"
        )

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse('userprofiles:signup')
        self.helper.form_id = 'form_profile'
        self.helper.form_class = 'forma'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            MultiField(
                'Llena los espacios',
                Div(
                    'first_name',
                    'last_name',
                    'username',
                    'email',
                    'password1',
                    'password2'
                ),
                'user_phone',
                'avatar',
                'calification'
            )
        )
        #self.fields['last_name'].label = 'Apellidos'
        #self.fields['email'].required = True
        #self.fields['email'].label = 'Tu correo'

        #self.fields['user_phone'].label = 'Teléfono'
        #self.fields['calification'].label = 'Calificación'


class UserCreationEmailForm(UserCreationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    # Checar que el email del usuario no exista


class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(EmailAuthenticationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse('userprofiles:signin')
        self.helper.form_id = 'form_login'
        self.helper.form_class = 'forma'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'email',
                'password'
            )
        )

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        self.user_cache = authenticate(username=email, password=password)

        if self.user_cache is None:
            raise forms.ValidationError('Usuario incorrecto')
        elif not self.user_cache.is_active:
            raise forms.ValidationError('Usuario inactivo')

        return self.cleaned_data

    def get_user(self):
        return self.user_cache


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
