""" Polished Pages forms. """
from django import forms
from django.utils.translation import ugettext_lazy as _
from polishedpages.models import BasicUser

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=_('Confirm password'),
        widget=forms.PasswordInput,
    )

    error_messages = {
        'password_mismatch': _("Passwords are not the same."),
    }

    class Meta:
        model = BasicUser
        fields = ('email',)

    def clean_password2(self):
        pw1 = self.cleaned_data['password1']
        pw2 = self.cleaned_data['password2']
        if pw1 != pw2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return pw2

    def save(self, commit=True):
        "Create the new user, setting the password as well."
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
