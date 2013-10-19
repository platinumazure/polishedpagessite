""" Polished Pages forms. """
from django import forms
from polishedpages.models import BasicUser

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput()
    )

    class Meta:
        model = BasicUser
        fields = ('email',)

    def clean_password2(self):
        pw1 = self.cleaned_data['password1']
        pw2 = self.cleaned_data['password2']
        if pw1 != pw2:
            raise forms.ValidationError("Passwords are not the same!")
        return pw2

    def save(self, commit=True):
        "Create the new user, setting the password as well."
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
