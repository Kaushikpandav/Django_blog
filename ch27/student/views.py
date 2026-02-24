from django.shortcuts import render
from student.form import register, login as LoginForm

# Create your views here.
def registration(request):
    form = register()
    return render(request, 'student/registration.html', {'form': form})

def login(request):
    # form = LoginForm(auto_id='login_%s')
    # form = LoginForm(auto_id=True)
    # form = LoginForm(initial={'username': 'username..', 'password': 'password..'}) #placeholder
    form = LoginForm(field_order=['password', 'username']) #change order of fields
    return render(request, 'student/login.html', {'form': form})