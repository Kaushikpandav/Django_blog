from django import forms
from .models import user


class userRegistrationForm(forms.ModelForm):

  CHOICES = (
    ('customer', 'customer'),
    ('seller', 'seller'),
  )
  role = forms.ChoiceField(choices=[CHOICES], required=True)
  password = forms.CharField(widget=forms.PasswordInput)
  confirm_password = forms.CharField(widget=forms.PasswordInput)

  class Meta:
    model = user
    fields = ['email', 'name', 'city', 'password', 'confirm_password']

  def clean(self):
      cleaned_data = super().clean()
      password = cleaned_data.get("password")
      confirm_password = cleaned_data.get("confirm_password")

      if password != confirm_password:
          self.add_error('confirm_password', "Passwords do not match.")
          raise forms.ValidationError("Passwords do not match.")

      return cleaned_data

  def clean_email(self):
      email = self.cleaned_data.get('email')
      if not email.endswith('.com'):
          raise forms.ValidationError("Email should be from the domain '.com'.")
      if user.objects.filter(email=email).exists():
          raise forms.ValidationError("Email already exists.")

      return email

class userLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)