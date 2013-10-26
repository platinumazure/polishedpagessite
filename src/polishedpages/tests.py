"""Unit tests for the polishedpages app."""
from django.test import TestCase
from django.contrib.auth.hashers import check_password
from .forms import RegistrationForm

class RegistrationFormTest(TestCase):
    def test_form_invalid_if_password2_not_equal_to_password1(self):
        """Form should not validate if password1 != password2."""
        # arrange
        target = RegistrationForm({
            'email': 'test@example.com',
            'password1': 'pw1',
            'password2': 'invalid',
        })

        # act
        result = target.is_valid()

        # assert
        self.assertFalse(result)

    def test_form_valid_if_password2_equals_password1(self):
        """Form should validate if password1 == password2, no other errors."""
        # arrange
        target = RegistrationForm({
            'email': 'test@example.com',
            'password1': 'passwd',
            'password2': 'passwd',
        })

        # act
        result = target.is_valid()

        # assert
        self.assertTrue(result)

    def test_form_saves_user_with_correct_password(self):
        """Form should create a new user with the correct password."""
        # arrange
        target = RegistrationForm({
            'email': 'test@example.com',
            'password1': 'passwd',
            'password2': 'passwd',
        })

        # act
        user = target.save()

        # assert
        self.assertTrue(check_password('passwd', user.password))
