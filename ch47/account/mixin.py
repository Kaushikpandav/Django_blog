from djnago.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect


class IsCustomerMixin(UserPassesTestMixin):
  def test_func(self):
    return self.request.user.is_authenticated and hasattr(self.request.user, 'is_customer') and self.request.user.

  def handle_no_permission(self):
    return redirect('login')

  def dispatch(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      return redirect('login')
    return super().dispatch(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      return redirect('login')
    return super().post(request, *args, **kwargs)

  def get(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      return redirect('login')
    return super().get(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      return redirect('login')
    return super().put(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      return redirect('login')
    return super().delete(request, *args, **kwargs)

  def patch(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      return redirect('login')
    return super().patch(request, *args, **kwargs)

  def head(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      return redirect('login')
    return super().head(request, *args, **kwargs)

  def options(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      return redirect('login')
    return super().options(request, *args, **kwargs)

  def trace(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      return redirect('login')
    return super().trace(request, *args, **kwargs)

  def connect(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      return redirect('login')
    return super().connect(request, *args, **kwargs)

  def trace(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      return redirect('login')
    return super().trace(request, *args, **kwargs)
