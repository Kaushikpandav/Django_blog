from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required



html_to_shown_on_unauthorized_request = """

<div class="alert alert-danger" role="alert">
    <h4 class="alert-heading">Unauthorized</h4>
    <p>You are not authorized to access this page.</p>
</div>

"""
def check_role(role):
  def decorator(view_func):
      @wraps(view_func)
      def _wrapped_view(request, *args, **kwargs):
          user  = request.user
          if role == 'customer' and not user.is_customer:
              return HttpResponseForbidden(html_to_shown_on_unauthorized_request)
          if role == 'seller' and not user.is_seller:
              return HttpResponseForbidden(html_to_shown_on_unauthorized_request)
          return view_func(request, *args, **kwargs)
