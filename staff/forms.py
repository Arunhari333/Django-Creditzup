from django import forms
from accounts.models import StaffProfile

class RegistrationForm2(forms.ModelForm):
    FirstName = forms.CharField()
    LastName = forms.CharField()
    Class = forms.CharField()
    Semester = forms.IntegerField()
    class Meta:
        model = StaffProfile
        fields = ('FirstName', 'LastName', 'Class', 'Semester')