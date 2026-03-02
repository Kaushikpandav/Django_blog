from .models import Profile

from django import forms

# regular form
# class StudentRegistrationForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

# # specific
# class StudentRegistrationForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

#     def clean_name(self):
#         name = self.cleaned_data.get('name')
#         if not name.isalpha():
#             raise forms.ValidationError("Name should only contain letters.")
#         return name

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if not email.endswith('.com'):
#             raise forms.ValidationError("Email should be from the domain '.com'.")
#         return email


# # validate all fields together
# class StudentRegistrationForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

#     def clean(self):
#         cleaned_data = super().clean()
#         name = cleaned_data.get('name')
#         email = cleaned_data.get('email')
#         password = cleaned_data.get('password')

#         if name and not name.isalpha():
#             self.add_error('name', "Name should only contain letters.")

#         if email and not email.endswith('.com'):
#             self.add_error('email', "Email should be from the domain '.com'.")

#         return cleaned_data



# custom validator and built-in validators
# from django.core import validators

# def start_with_a(value):
#     if not value.startswith('A'):
#         raise validators.ValidationError("Value should start with 'A'.")

# # Built-in validators and custom validator
# class StudentRegistrationForm(forms.Form):
#     name = forms.CharField(max_length=100, validators=[validators.RegexValidator(regex='^[a-zA-Z]+$', message='Name should only contain letters.'), validators.MinLengthValidator(2, message='Name should be at least 2 characters long.')])
#     email = forms.EmailField(validators=[start_with_a])
#     password = forms.CharField(widget=forms.PasswordInput)



# django Model Form
# class StudentRegistrationForm(forms.ModelForm):

#     # to override model
#     name = forms.CharField(max_length=200)

#     # extra field | this will not bale to store in DB it's just to map same logic
#     confirm_pass = forms.CharField(
#         widget=forms.PasswordInput()
#     )

#     class Meta:
#         model = Profile

#         # fields = ['name', 'email', 'password']
#         # if i want to include all fields then i can use __all__
#         fields = '__all__'

#         # if i want to exclude any field then i can use exclude
#         # exclude = ['confirm_pass']

#         # if i want to change label or error message or widget then i can use below code
#         labels = {
#             'name': 'Full Name',
#             'email': 'Email Address',
#             'password': 'Password',
#         }
#         error_messages = {
#             'email' : {'required':'field required'}
#         }
#         widgets = {
#             'password':forms.PasswordInput(attrs={
#                 'class':'pwdclass'
#             }),
#             'name':forms.TextInput(attrs={
#                 'class':'pwdclass', 'placeholder':'enter your name..'
#             })
#         }


# django model inheritance form

class StudentRegistrationForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['student_name', 'email', 'password']

class TeacherRegistrationForm(StudentRegistrationForm):
  class Meta(StudentRegistrationForm.Meta):
    fields = ['teacher_name', 'email', 'password']