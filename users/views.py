from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import update_session_auth_hash
from django.views.generic import View, UpdateView
from users.forms import UserPasswordChangeForm, CustomUserForm
from users.models import CustomUser


class UserLoginView(LoginView):
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        context['admin'] = True
        context['banner'] = 'studentBanner'
        return context


class UserLogoutView(LogoutView):
    http_method_names = ['post']


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'users/edit_profile.html'
    form_class = CustomUserForm
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Profile'
        context['admin'] = True
        context['banner'] = 'studentBanner'
        return context

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse('students:list')


class UserPasswordChangeView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'form': UserPasswordChangeForm(self.request.user),
            'title': 'Change Password',
            'admin': True,
            'banner': 'studentBanner'
        }
        return render(request, 'users/password_change.html', context=context)

    def post(self, request):
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(self.request, form.user)
            return redirect('students:list')

        context = {'form': form, 'title': 'Change Password', 'admin': True, 'banner': 'studentBanner'}
        return render(request, 'users/password_change.html', context=context)
