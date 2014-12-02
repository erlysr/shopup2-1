from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, RedirectView

from . import forms
from . models import UserProfile


class RegisterProfile(FormView):
    """
    Vista de registro tradicional de usuario (form)
    """
    template_name = 'signup.html'
    form_class = forms.ProfileForm

    def form_invalid(self, form):
        print '#' * 10, 'invalido'
        print form.errors
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        # username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        telefono = form.cleaned_data['user_phone']
        avatar = form.cleaned_data['avatar']
        calificacion = form.cleaned_data['calification']
        # Guardar django.contrib.auth.models.User
        user = form.save()

        # Crear Perfil a partir del user creado
        profile = UserProfile(
            username=user,
            user_phone=telefono,
            avatar=avatar,
            calification=calificacion
        )
        profile.save()
        usuario = authenticate(username=user.email, password=password)
        login(self.request, usuario)
        return redirect('/')


def signup(request):
    form = forms.UserCreationEmailForm(request.POST or None)

    if form.is_valid():
        form.save()

    # Aqui loguear el usuario
    # Crear el userprofile, con avatar y todo eso
    # redireccionar al home

    return render(request, 'signup.html', {'form': form})


# def signin(request):
#     form = EmailAuthenticationForm(request.POST or None)

#     if form.is_valid():
#         #loguear
#         login(request, form.get_user())

#         #redireccionar al home

#     return render(request, 'signin.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


class ProfileView(TemplateView):

    template_name = 'login_in.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        is_auth = False
        name = None
        lastname = None

        if self.request.user.is_authenticated():
            is_auth = True
            name = self.request.user.first_name
            lastname = self.request.user.last_name

            data = {
                'is_auth': is_auth,
                'name': name,
                'lastname': lastname,
                'userprofile': self.get_userprofile()
            }

            context.update(data)

            if self.get_userprofile() is None:
                self.template_name = 'ProfileSignUp.html'

            return context

    def get_userprofile(self):
        try:
            userprofile = self.request.user.userprofile
        except:
            return None
        else:
            return userprofile


class LoginView(FormView):

    form_class = forms.EmailAuthenticationForm
    template_name = 'login.html'
    success_url = '/profile/'

    def form_valid(self, form):
        #email = form.cleaned_data['email']
        #password = form.cleaned_data['password']
        #user = authenticate(email=email, password=password)
        #falta validar si el usuario tiene userprofile o si no hay sesion
        login(self.request, form.user_cache)
        admin = form.user_cache.is_superuser
        if admin:
            self.success_url = '/admin/'
        return super(LoginView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        is_auth = False
        name = None
        lastname = None

        if self.request.user.is_authenticated():
            is_auth = True
            name = self.request.user.first_name
            lastname = self.request.user.last_name

            data = {
                'is_auth': is_auth,
                'name': name,
                'lastname': lastname,
                'userprofile': self.get_userprofile()
            }
            if self.get_userprofile() is None:
                #   self.template_name = 'profilesignup.html'
                self.success_url = '/profilesignup/'
            context.update(data)
        return context

    def get_userprofile(self):
        try:
            userprofile = self.request.user.userprofile
        except ObjectDoesNotExist:
            userprofile = None

        return userprofile


class PerfilRedirectView(RedirectView):
    pattern_name = 'perfil'
