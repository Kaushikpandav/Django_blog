

# To restrict access we use decorators for functions based view but in class based view we use mixins


from djnago.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect


class IsCustomerMixin(UserPassesTestMixin):

  #if this failled it will go to handle_no_permission
  def test_func(self):
    return self.request.user.is_authenticated and hasattr(self.request.user, 'is_customer') and self.request.user.is_customer

  def handle_no_permission(self):
    if self.request.user.is_authenticated:
      return HttpResponseForbidden("""Access Denied""")
    return redirect('login')

class IssellerMixin(UserPassesTestMixin):

  #if this failled it will go to handle_no_permission
  def test_func(self):
    return self.request.user.is_authenticated and hasattr(self.request.user, 'is_seller') and self.request.user.is_seller

  def handle_no_permission(self):
    if self.request.user.is_authenticated:
      return HttpResponseForbidden("""Access Denied""")
    return redirect('login')