from pyexpat.errors import messages

from django.shortcuts import render
from django.contrib.auth.view import PasswordChangeView
from django.contrib.auth import logout
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class CustomeDashbordView(View, LoginRequiredMixin):
  def get(self, request):
    return render(request, 'customer/dashboard.html')


class ChangePasswordChangeView(PasswordChangeView, LoginRequiredMixin):
  template_name = 'customer/changepassword.html'
  success_url = '/Login/'

  def form_valid(self, form):
    res =  super().form_valid(form)
    logout(self.request)
    messages.success(self.request, 'Password changed successfully.')
    return res

  def form_invalid(self, form):
    res = super().form_invalid(form)
    messages.error(self.request, 'Failed to change password.')
    return res