from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_password2(self):
        if self.cleaned_data['password2'] != self.cleaned_data['password']:
            raise forms.ValidationError('Passwords Mismatch')

    def save(self, commit=True):
        user = super().save(commit)
        if commit:
            user.set_password(self.cleaned_data['password'])
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_form(self):
        email = self.cleaned_data.get('email', '')
        password = self.cleaned_data.get('password', '')

        user = User.objects.filter(email=email).first()
        if not user:
            raise forms.ValidationError('Incorrect email.')

        if not user.check_password(password):
            raise forms.ValidationError('Incorrect password.')

        return self.cleaned_data