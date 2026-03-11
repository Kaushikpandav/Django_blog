from urllib import request
from django.shortcuts import render
from ch40.core.decoreators import check_role

@check_role('customer')
def getdashboard(request):
  return render(request, 'customer/dashboard.html')
