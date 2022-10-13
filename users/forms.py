from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    error_messages = {'password_error': "The two password fields didn't match"}
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(),
        required=True
    )
    new_password = forms.CharField(
        max_length=24,
        label='Type new password',
        widget=forms.PasswordInput(),
        required=True
    )
    confirm_password = forms.CharField(
        max_length=24,
        label='Confirm your password',
        widget=forms.PasswordInput(),
        required=True
    )

    class Meta:
        model = User
        fields = ('email', 'new_password', 'confirm_password',)

    def is_valid(self):
        if not self.errors:
            new_password = self.cleaned_data['new_password']
            conform_password = self.cleaned_data['confirm_password']
            if new_password is True and conform_password is True and new_password != conform_password: # noqa
                self.errors.update(self.error_messages)
        return super().is_valid()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.set_password(self.cleaned_data["new_password"])
        if commit:
            user.save()
        return user