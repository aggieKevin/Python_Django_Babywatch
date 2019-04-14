from django import forms
from django.contrib.auth.models import User
from .models import Household,Guardian,Child,Rating


class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password"),
        widget=forms.PasswordInput,
        help_text=("Enter the same password as above, for verification.")
        )


    class Meta:
        model = User
        fields = ("username",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class HouseholdForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    class Meta:
        model = Household
        exclude=('user',)


class GuardianForm(forms.ModelForm):
    class Meta:
        model=Guardian
        exclude=('household',)

class ChildForm(forms.ModelForm):
    class Meta:
        model=Child
        exclude=('household',)


    '''
    def save(self, commit=True):
        household=self.save(commit=False)
        household.address_line1=self.cleaned_data('address_line1')
        household.address_line2=self.cleaned_data('address_line2')
        household.city=self.cleaned_data('city')
        household.state=self.cleaned_data('state')
        household.zip=self.cleaned_data('zip')
        household.email=self.cleaned_data('email')
        if commit:
            household.save()
        return household
    '''
class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude=('receiver','giver')
