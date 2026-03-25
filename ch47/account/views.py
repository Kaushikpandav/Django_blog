from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView
from .form import Register
from django.shortcuts import redirect
# Create your views here.

from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from ch40.account.utils import send_activation_email
from django.conf import settings
from django import messages, views

from .utils import send_activation_email
from djnago.contrib.auth import authenticate, login


# this mixin secure view by proteting with loging and fore role based APi we use : from djnago.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
# to redirect this loginrequire to out actually login page we need to do this in settings.py :
# LOGIN_URL = 'login'

class RegisterView(FormView, LoginRequiredMixin):
  template_name = 'account/register.html'
  form_class = Register

  def form_valid(self, form):
    user = form.save(commit=False)
    user.set_password(form.cleaned_data['password'])
    user.is_active = False
    user.save()

    # send verification email
    uid64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    activation_link = reverse('activate', kwargs={'uidb64': uid64, 'token': token})

    # send email
    link = f'{settings.SITE_URL}{activation_link}'
    send_activation_email(user.email, link)

    send_activation_email(user.email, link)
    messages.success(self.request, 'Account created successfully. Please check your email to activate your account.')
    return redirect('login')


  # Account Activation
def activate(request, uidb64, token, ):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user_instance = user.objects.get(pk=uid)

        if user_instance.is_active:
            messages.warning(request, 'Account already activated.')
            return redirect('login')

        if user_instance is not None and default_token_generator.check_token(user_instance, token):
            user_instance.is_active = True
            user_instance.save()
            messages.success(request, 'Account activated successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Invalid activation link.')
            return redirect('register')

    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        messages.error(request, 'Invalid activation link.')
        return redirect('register')

class LoginView(views):
  template_name = 'account/login.html'

  def dispatch(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect(self.get_success_url())

  def get_success_url(self):
    if self.request.user.is_superuser:
      return reverse('admin:index')
    if self.request.user.is_customer:
      return reverse('customer')
    if self.request.user.is_seller:
      return reverse('seller')
    return reverse('home')

  def get(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect(self.get_success_url())
    return super().get(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if not email or not password:
      messages.error(request, 'Email and password are required.')
      return redirect('login')

    try:
      user_instance = user.objects.get(email=email)
    except user.DoesNotExist:
      messages.error(request, 'User does not exist.')
      return redirect('login')

    if not user_instance.is_active:
      messages.error(request, 'Account is not active. Please check your email to activate your account.')
      return redirect('login')

    user = authenticate(request, email=email, password=password)

    if user is not None:
      login(request, user)
      return redirect(self.get_success_url())


class CustomPasswordResetView(views, LoginRequiredMixin):
  template_name = 'account/password_reset.html'
  form_class = resetpassword
  success_url = reverse_lazy('password_reset_done')

  def form_valid(self, form):
    email = form.cleaned_data['email']
    user = user.objects.filter(email=email).first()
    if user:
      reseturl = self.get_reset_url(user)
      link = f'{settings.SITE_URL}{reseturl}'
      send_activation_email(user.email, link)
    return super().form_valid(form)

  def get_reset_url(self, user):
    uid64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uid64, 'token': token})
    return f"{self.request.build_absolute_uri(reset_url)}"

class PasswordResetConfirmView(views, LoginRequiredMixin):
  template_name = 'account/password_reset_confirm.html'

  def get(self, request, uidb64, token):
    try:
      uid = force_str(urlsafe_base64_decode(uidb64))
      user_instance = user.objects.get(pk=uid)

      if user_instance is not None and default_token_generator.check_token(user_instance, token):
        form = SetPasswordForm(user = user_instance)
        return render(request, self.template_name, {'uidb64': uidb64, 'token': token})
      else:
        messages.error(request, 'Invalid reset link.')
        return redirect('login')

    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
      messages.error(request, 'Invalid reset link.')
      return redirect('login')

  def post(self, request, uidb64, token):
    try:
      uid = force_str(urlsafe_base64_decode(uidb64))
      user_instance = user.objects.get(pk=uid)

      if user_instance is not None and default_token_generator.check_token(user_instance, token):
        form = SetPasswordForm(user = user_instance, data = request.POST)
        if form.is_valid():
          form.save()
          messages.success(request, 'Password reset successfully.')
          return redirect('login')
        else:
          for index, errors in form.errors.items():
            for error in errors:
              messages.error(request, error)
      else:
        messages.error(request, 'Invalid reset link.')
        return redirect('login')

    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
      messages.error(request, 'Invalid reset link.')
      return redirect('login')