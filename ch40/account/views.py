from django.shortcuts import redirect, render
from .forms import userRegistrationForm, userLoginForm
from django.contrib import messages
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str
from django.urls import reverse
from .utils import send_activation_email
from core.utils import assign_permission

# inbuilt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.decorators import login_required

from .models import user


@login_required
def home(request):
  form = userRegistrationForm()
  return render(request, 'account/home.html', {'form': form})

# Registration View
def register(request):
    if request.method == 'POST':
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            user_instance = form.save(commit=False)
            user_instance.set_password(form.cleaned_data['password'])
            user_instance.is_active = False

            role = form.cleaned_data['role']
            if role == 'customer':
                user_instance.is_customer = True
                user_instance.is_seller = False
            elif role == 'seller':
                user_instance.is_customer = False
                user_instance.is_seller = True
                user_instance.is_staff = True

            user_instance.save()

            assign_permission(user_instance, role)

            messages.success(request, 'Registration successful. Please check your email for verification.')

            uid64 = urlsafe_base64_encode(force_bytes(user_instance.pk))
            token = default_token_generator.make_token(user_instance)

            link = reverse('activate', kwargs={'uidb64': uid64, 'token': token})
            complete_link = f'{settings.SITE_URL}{link}'

            send_activation_email(user_instance.email, complete_link)
            return redirect('login')
    else:
       form = userRegistrationForm()

    return render(request, 'account/register.html', {'form': form})

# Account Activation
def activate(request, uidb64, token):
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

# Login View
def login_view(request):
  if request.user.is_authenticated:
    if request.user.is_superuser:
      return redirect('admin:index')
    if request.user.is_customer:
      return redirect('customer')
    if request.user.is_seller:
      return redirect('seller')
    return redirect('home')

  if request.method == 'POST':
    form = userLoginForm(request.POST)
    if form.is_valid():
      email = form.cleaned_data.get('email')
      password = form.cleaned_data.get('password')

      try :
        user_instance = user.objects.get(email=email)
      except user.DoesNotExist:
        messages.error(request, 'Invalid email or password.')
        return redirect('login')

      if not user_instance.is_active:
        messages.error(request, 'Account is not active.')
        return redirect('login')

      auth_user = authenticate(request, email=email, password=password)

      if auth_user is not None:
        login(request, auth_user)
        if auth_user.is_superuser:
            return redirect('admin:index')
        if auth_user.is_seller:
            return redirect('seller')
        if auth_user.is_customer:
            return redirect('customer')
        return redirect('home')
      else:
        messages.error(request, 'Invalid email or password.')
        return redirect('login')
  else:
    form = userLoginForm()
  return render(request, 'account/login.html', {'form': form})


# Password Change
@login_required
def changepassword(request):
  if request.method == 'POST':
    form = PasswordChangeForm(user = request.user, data = request.POST)
    if form.is_valid():
      form.save()
      logout(request)
      messages.success(request,'Password changed successfully.')
      return redirect('login')
    else:
      for i , errors in form.errors.items():
        for error in errors:
          messages.error(request, error)
      return redirect('login')
  else:
    form = PasswordChangeForm(user = request.user)
  return render(request, 'account/changepassword.html', {'form': form})


# Password Reset confirm
def password_reset_confirm(request, uidb64, token):
  try:
    uid = force_str(urlsafe_base64_decode(uidb64))
    user_instance = user.objects.get(pk=uid)

    if user_instance is not None and default_token_generator.check_token(user_instance, token):
      if request.method == 'POST':
        form = SetPasswordForm(user_instance, request.POST)
        if form.is_valid():
          form.save()
          messages.success(request, 'Password reset successfully.')
          return redirect('login')
        else:
          for index, errors in form.errors.items():
            for error in errors:
              messages.error(request, error)
      else:
        form = SetPasswordForm(user_instance)
      return render(request, 'account/password_reset_confirm.html', {'form': form})

  except (TypeError, ValueError, OverflowError, user.DoesNotExist):
    messages.error(request, 'Invalid reset link.')
  return render(request, 'account/password_reset_confirm.html')
