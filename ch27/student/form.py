from django import forms

class register(forms.Form):
  first_name = forms.CharField(max_length=100)
  last_name = forms.CharField(max_length=100)
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput)
  city = forms.CharField(max_length=100)

  def clean_email(self):
    email = self.cleaned_data.get('email')
    if not email.endswith('@gmail.com'):
      raise forms.ValidationError('Email must be a gmail address')
    return email

class login(forms.Form):
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput)
