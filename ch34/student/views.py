from django.shortcuts import render
from .form import StudentRegistrationForm, TeacherRegistrationForm
from .models import Profile
# Create your views here.
def register(request):

    if request.method == 'POST':
        print("Form data:", request.POST.get('name'), request.POST.get('email'), request.POST.get('password'))  # Debugging line to check form data

        form = StudentRegistrationForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            con_pass = form.cleaned_data['confirm_pass']

            # save DB
            # p = Profile(name=name, email=email, password=password)
            # p.save()
            # or
            Profile.objects.create(name=name, email=email, password=password, confirm_pass=con_pass)

            # update
            # Profile.objects.filter(email=email).update(name=name, email=email, password=password) or
            # user  = Profile(id=3, name=name, email=email, password=password)
            # user.save()

            # delete
            # delete_user = Profile(id=1)
            # delete_user.delete()

            # return HttpResponseRedirect('/student')
            return render(request, 'success.html', {'name': name})
    else:
      form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})


# model form inheritance view
def register(request):

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():

            student_name = form.cleaned_data['student_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # save DB
            Profile.objects.create(student_name=student_name, email=email, password=password)

            return render(request, 'success.html', {'name': student_name})
    else:
      form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})

def teacher_register(request):

    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():

            teacher_name = form.cleaned_data['teacher_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # save DB
            Profile.objects.create(teacher_name=teacher_name, email=email, password=password)

            return render(request, 'success.html', {'name': teacher_name})
    else:
      form = TeacherRegistrationForm()
    return render(request, 'register.html', {'form': form})