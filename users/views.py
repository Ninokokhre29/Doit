from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.views.generic import FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm, ProfileForm
from .models import Profile

class LogoutUserView(LoginRequiredMixin, FormView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('users:login')

class LoginUserView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('shop:index')

class RegisterUserView(FormView):
    form_class = RegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('shop:index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class ProfileView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request):
        profile, _ = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(instance=profile)
        password_form = PasswordChangeForm(user=request.user)
        context = {
            'profile': profile,
            'profile_form': profile_form,
            'password_form': password_form
        }
        return render(request, 'users/profile.html', context)

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if 'update_profile' in request.POST:
            if profile_form.is_valid():
                profile_form.save()
                return redirect('users:profile')
            else:
                password_form = PasswordChangeForm(user=request.user)
                context = {
                    'profile': profile,
                    'profile_form': profile_form,
                    'password_form': password_form
                }
                return render(request, 'users/profile.html', context)

        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if 'change_password' in request.POST:
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                return redirect('users:profile')
            else:
                profile_form = ProfileForm(instance=profile)
                context = {
                    'profile': profile,
                    'profile_form': profile_form,
                    'password_form': password_form
                }
                return render(request, 'users/profile.html', context)


        return redirect('users:profile')
