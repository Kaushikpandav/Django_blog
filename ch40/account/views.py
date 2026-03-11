from django.shortcuts import redirect, render
from .forms import userRegistrationForm
from django.contrib import messages
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str
from django.urls import reverse
from utils import send_activation_email

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm, PasswordChangeFormrequest
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm

from .models import user


@login_required
def home(request):
  form = userRegistrationForm()
  return render(request, 'account/home.html', {'form': form})

@login_required
def register(request):
    if request.method == 'POST':
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False

            role = form.cleaned_data['role']
            if role == 'customer':
                user.is_customer = True
                user.is_seller = False
            elif role == 'seller':
                user.is_customer = False
                user.is_seller = True

            user.save()
            messages.success(request, 'Registration successful. Please check your email for verification.')

            uid64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            link = reverse('activate', kwargs={'uidb64': uid64, 'token': token})
            complete_link = f'{settings.SITE_URL}{link}'

            send_activation_email(user.email, complete_link)
            return redirect('login')
    else:
       form = userRegistrationForm()

    return render(request, 'account/register.html', {'form': form})

@login_required
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = user.objects.get(pk=uid)

        if user.is_active:
            messages.warning(request, 'Account already activated.')
            return redirect('login')

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Account activated successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Invalid activation link.')
            return redirect('register')

    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        messages.error(request, 'Invalid activation link.')
        return redirect('register')

@login_required
def login_view(request):

  if request.user.is_authenticated:
    if request.user.is_superuser:
      return redirect('admin')
    if request.user.is_staff:
      return redirect('staff')
    if request.user.is_customer:
      return redirect('customer')
    if request.user.is_seller:
      return redirect('seller')
    return redirect('home')

  if request.method == 'POST':
    form = userRegistrationForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']

      if username or password is None:
        messages.error(request, 'Invalid username or password.')

      try :
        user = user.objects.get(username=username)
      except:
        messages.error(request, 'Invalid username or password.')

      if not user.is_active:
        messages.error(request, 'Account is not active.')
        return redirect('login')

      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)
        if user.is_superuser:
          return redirect('admin')
        if user.is_staff:
          return redirect('staff')
        if user.is_customer:
          return redirect('customer')
        if user.is_seller:
          return redirect('seller')
        return redirect('home')
      else:
        messages.error(request, 'Invalid username or password.')
        return redirect('login')
  return render(request, 'account/login.html', {'form': form})


# logout
# already done via inbuilt function in urls file

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


# protect your API with :

# from django.contrib.auth.decorators import login_required
# @login_required


# reset password
def password_reset_confirm(request, uidb64, token):

  try:
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = user.objects.get(pk=uid)

    if user is not None and default_token_generator.check_token(user, token):
      if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
          form.save()
          messages.success(request, 'Password reset successfully.')
          return redirect('login')
        else:
          for index, errors in form.errors.items():
            for error in errors:
              messages.error(request, error)
      else:
        form = SetPasswordForm(user)
      return render(request, 'account/password_reset_confirm.html', {'form': form})

  except (TypeError, ValueError, OverflowError, user.DoesNotExist):
    messages.error(request, 'Invalid reset link.')
  return render(request, 'account/password_reset_confirm.html')
