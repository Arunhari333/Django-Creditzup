from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import UserProfile, LeadPage, CultPage, ProfPage, EntrePage, GamePage, NatPage

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User

        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        if commit:
            user.save()

        return user

class RegistrationForm2(forms.ModelForm):
    FirstName = forms.CharField()
    LastName = forms.CharField()
    Class = forms.CharField()
    Semester = forms.IntegerField()
    class Meta:
        model = UserProfile
        fields = ('FirstName', 'LastName', 'Class', 'Semester')

class EditprofileForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = ('FirstName', 'LastName', 'Class', 'Semester')

class LeadForm(forms.ModelForm):
    CHOICE = ((0, 'Select:'),
              (1, 'Student Professional Societies (IEEE, IET, ASME, SAE, NASA etc.)'),
              (2, 'College Association Chapters (Mechanical, Civil,Electrical etc.)'),
              (3, 'Festival & Technical Events(College approved)'),
              (4, 'Hobby Clubs'),
              (5, 'Special Initiatives(Approval from College and University is mandatory)'))

    CHOICE1 = ((0, 'Select:'), (1, 'Core coordinator'), (2, 'Sub coordinator'), (3, 'Volunteer'))

    CHOICE2 = ((0, 'Select:'), (1, '(a) Certificate'), (2, '(b) Letter from Authorities'),
               (3, '(c) Appreciation recognition letter'), (4, '(d)Documentary evidence'),
               (5, '(e) Legal Proof'), (6, 'Others'))

    Category = forms.IntegerField(widget=forms.Select(choices=CHOICE))
    SubCategory = forms.IntegerField(widget=forms.Select(choices=CHOICE1))
    DocType = forms.IntegerField(widget=forms.Select(choices=CHOICE2))
    File = forms.FileField(required=True)
    Approved = forms.BooleanField(widget=forms.HiddenInput())

    class Meta:
        model = LeadPage
        fields = ('Category', 'SubCategory', 'DocType', 'File', 'Approved')

class Cultform(forms.ModelForm):
    CHOICE = ((1, 'Yes'), (2, 'No'))
    CHOICE1 = ((0, 'Select:'), (1, 'Music'), (2, 'Performing Arts'), (3, 'Literary Arts'))
    CHOICE2 = ((0, 'Select:'), (1, 'College Events'), (2, 'Zonal Events'), (3, 'State/ University Events'),
               (4, 'National Events'), (5, 'International Events'))
    CHOICE3 = ((0, 'Select:'), (1, 'First'), (2, 'Second'), (3, 'Third'))
    CHOICE4 = ((0, 'Select:'), (1, '(a) Certificate'), (2, '(b) Letter from Authorities'),
               (3, '(c) Appreciation recognition letter'), (4, '(d)Documentary evidence'),
               (5, '(e) Legal Proof'), (6, 'Others')
               )

    OneYear = forms.CharField(widget=forms.RadioSelect(choices=CHOICE))
    Category = forms.CharField(widget=forms.Select(choices=CHOICE1))
    Level = forms.CharField(widget=forms.Select(choices=CHOICE2))
    Position = forms.CharField(widget=forms.Select(choices=CHOICE3))
    DocType = forms.CharField(widget=forms.Select(choices=CHOICE4))
    File = forms.FileField(required=True)
    Approved = forms.BooleanField(widget=forms.HiddenInput())

    class Meta:
        model = CultPage
        fields = ('OneYear', 'Category', 'Level', 'Position', 'DocType', 'File', 'Approved')

class Profform(forms.ModelForm):
    CHOICE = ((0, 'Select:'),
              (1, 'Tech Fest, Tech Quiz'),
              (2, 'MOOC with final assessment certificate'),
              (3, 'Competitions conducted by Professional Societies - (IEEE, IET, ASME, SAE, NASA etc.)'),
              (4, 'Attending Full time Conference/Seminars /Exhibitions/Workshop/STTP conducted at IITs/NITs'),
              (5, 'Paper presentation/publication at IITs/NITs'),
              (6, 'Poster Presentation at IITs /NITs'),
              (7, 'Industrial Training/Internship (at least for 5 full days)'),
              (8, 'Industrial/Exhibition visits'),
              (9, 'Foreign Language Skill (TOFEL/IELTS/BEC exams etc.)'))
    CHOICE1 = ((0, 'Select'), (1, 'College Events'), (2, 'Zonal Events'), (3, 'State/ University Events'),
               (4, 'National Events'), (5, 'International Events'))
    CHOICE2 = ((0, 'Select:'), (1, '(a) Certificate'), (2, '(b) Letter from Authorities'),
               (3, '(c) Appreciation recognition letter'), (4, '(d)Documentary evidence'),
               (5, '(e) Legal Proof'), (6, 'Others')
               )

    Category = forms.CharField(widget=forms.Select(choices=CHOICE))
    Level = forms.CharField(widget=forms.Select(choices=CHOICE1))
    DocType = forms.CharField(widget=forms.Select(choices=CHOICE2))
    File = forms.FileField(required=True)
    Approved = forms.BooleanField(widget=forms.HiddenInput())

    class Meta:
        model = ProfPage
        fields = ('Category', 'Level', 'DocType', 'File', 'Approved')

class Entreform(forms.ModelForm):
    CHOICE = ((0, 'Select:'),
              (1, 'Start-up Company –Registered legally'),
              (2, 'Patent-Filed'),
              (3, 'Patent-Published'),
              (4, 'Patent-Approved'),
              (5, 'Patent-Licensed'),
              (6, 'Prototype developed and tested'),
              (7, 'Awards for Products developed'),
              (8, 'Innovative technologies developed and used by industries/users'),
              (9, 'Got venture capital funding for innovative ideas/products'),
              (10, 'Startup Employment (Offering jobs to two persons less than Rs. 15000/- per month)'),
              (11, 'Societal innovations'))

    CHOICE1 = ((0, 'Select:'), (1, '(a) Certificate'), (2, '(b) Letter from Authorities'),
               (3, '(c) Appreciation recognition letter'), (4, '(d)Documentary evidence'),
               (5, '(e) Legal Proof'), (6, 'Others'))

    Category = forms.CharField(widget=forms.Select(choices=CHOICE))
    DocType = forms.CharField(widget=forms.Select(choices=CHOICE1))
    File = forms.FileField(required=True)
    Approved = forms.BooleanField(widget=forms.HiddenInput())

    class Meta:
        model = EntrePage
        fields = ('Category', 'DocType', 'File', 'Approved')

class Gameform(forms.ModelForm):
    CHOICE = ((1, 'Yes'), (2, 'No'))
    CHOICE1 = ((0, 'Select:'), (1, 'Sports'), (2, 'Games'))
    CHOICE2 = ((0, 'Select:'), (1, 'College Events'), (2, 'Zonal Events'), (3, 'State/ University Events'),
               (4, 'National Events'), (5, 'International Events'))
    CHOICE3 = ((0, 'Select:'), (1, 'First'), (2, 'Second'), (3, 'Third'))
    CHOICE4 = ((0, 'Select:'), (1, '(a) Certificate'), (2, '(b) Letter from Authorities'),
               (3, '(c) Appreciation recognition letter'), (4, '(d)Documentary evidence'),
               (5, '(e) Legal Proof'), (6, 'Others')
               )

    OneYear = forms.CharField(widget=forms.RadioSelect(choices=CHOICE))
    Category = forms.CharField(widget=forms.Select(choices=CHOICE1))
    Level = forms.CharField(widget=forms.Select(choices=CHOICE2))
    Position = forms.CharField(widget=forms.Select(choices=CHOICE3))
    DocType = forms.CharField(widget=forms.Select(choices=CHOICE4))
    File = forms.FileField(required=True)
    Approved = forms.BooleanField(widget=forms.HiddenInput())

    class Meta:
        model = GamePage
        fields = ('OneYear', 'Category', 'Level', 'Position', 'DocType', 'File', 'Approved')

class NatForm(forms.ModelForm):
    CHOICE = ((1, 'Yes'), (2, 'No'))
    CHOICE1 = ((0, 'Select:'), (1, 'NCC'), (2, 'NSS'))
    CHOICE2 = ((0, 'Select:'),
               (1, 'C certificate(os performance)'),
               (2, 'Best NSS Volunteer Awardee(University Level)'),
               (3, 'Participation in National Integration Camp'),
               (4, 'Participation in Pre-Republic Day Parade Camp'),
               (5, 'Best NSS Awardee(State Level/National Level)'),
               (6, 'Participation in Republic Day Parade Camp'),
               (7, 'International Youth Exchange Programme'),
               (8, 'Others'))
    CHOICE3 = ((0, 'Select:'), (1, '(a) Certificate'), (2, '(b) Letter from Authorities'),
               (3, '(c) Appreciation recognition letter'), (4, '(d)Documentary evidence'),
               (5, '(e) Legal Proof'), (6, 'Others'))

    TwoYears = forms.CharField(widget=forms.RadioSelect(choices=CHOICE))
    Category = forms.CharField(widget=forms.Select(choices=CHOICE1))
    SubCategory = forms.CharField(widget=forms.Select(choices=CHOICE2))
    DocType = forms.CharField(widget=forms.Select(choices=CHOICE3))
    File = forms.FileField(required=True)
    Approved = forms.BooleanField(widget=forms.HiddenInput())

    class Meta:
        model = NatPage
        fields = ('TwoYears', 'Category', 'SubCategory', 'DocType', 'File', 'Approved')
