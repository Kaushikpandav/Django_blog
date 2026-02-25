from django import forms



# specific
class StudentRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isalpha():
            raise forms.ValidationError("Name should only contain letters.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('.com'):
            raise forms.ValidationError("Email should be from the domain '.com'.")
        return email


# validate all fields together
class StudentRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if name and not name.isalpha():
            self.add_error('name', "Name should only contain letters.")

        if email and not email.endswith('.com'):
            self.add_error('email', "Email should be from the domain '.com'.")

        return cleaned_data