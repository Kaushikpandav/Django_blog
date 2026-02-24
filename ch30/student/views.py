from django.shortcuts import render
from .form import StudentRegistrationForm
# Create your views here.
def register(request):

    if request.method == 'POST':
        print("Form data:", request.POST.get('name'), request.POST.get('email'), request.POST.get('password'))  # Debugging line to check form data

        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save to database)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Here you would typically save the data to the database
            return render(request, '/student/success.html', {'name': name})
    else:
      form = StudentRegistrationForm()
    return render(request, 'student/register.html', {'form': form})