from urllib import request

from django.shortcuts import render
from ch40.core.decoreators import check_role
# Create your views here.


@check_role('seller')
def getdashboard(request):
  return render(request, 'seller/dashboard.html')