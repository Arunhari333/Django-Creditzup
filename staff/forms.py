from django import forms
from staff.models import StaffProfile

class RegistrationForm2(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ('FirstName', 'LastName', 'Class', 'Semester')
