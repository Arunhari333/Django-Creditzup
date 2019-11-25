from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
    User,
    models.SET_NULL,
    blank=True,
    null=True,
)
    FirstName = models.CharField(max_length=100, default='')
    LastName = models.CharField(max_length=100, default='')
    Class = models.CharField(max_length=100, default='')
    Semester = models.IntegerField(default=0)
    TotalCredits = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.user)

    # def create_profile(sender, **kwargs):
    #     if kwargs['created']:
    #         user_profile = UserProfile.objects.create(user=kwargs['instance'])
    #
    # post_save.connect(create_profile, sender=User)

class LeadPage(models.Model):

    CHOICE = ((0,'Select:'),
              (1, 'Student Professional Societies (IEEE,IET, ASME, SAE,NASA etc.)'),
              (2, 'College Association Chapters (Mechanical, Civil,Electrical etc.)'),
              (3, 'Festival & Technical Events(College approved)'),
              (4, 'Hobby Clubs'),
              (5, 'Special Initiatives(Approval from College and University is mandatory)'),
              )
    CHOICE1 = ((0,'Select:'), (1, 'Core coordinator'), (2, 'Sub coordinator'), (3, 'Volunteer'))
    CHOICE2 = ((0,'Select:'), (1, '(a) Certificate'), (2, '(b) Letter from Authorities'),
               (3, '(c) Appreciation recognition letter'), (4, '(d)Documentary evidence'),
               (5, '(e) Legal Proof'), (6, 'Others')
               )

    user1 = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    Category = models.IntegerField(choices=CHOICE, default=0)
    SubCategory = models.IntegerField(choices=CHOICE1, default=0)
    DocType = models.IntegerField(choices=CHOICE2, default=0)
    File = models.FileField(null=True, blank=True)
    Approved = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.user1)

class CultPage(models.Model):
    CHOICE = ((1, 'Yes'), (2, 'No'))
    CHOICE1 = ((0,'Select:'),(1, 'Music'),(2, 'Performing Arts'),(3, 'Literary Arts'))
    CHOICE2 = ((0,'Select:'), (1, 'College Events'), (2, 'Zonal Events'), (3, 'State/ University Events'),
               (4, 'National Events'),(5, 'International Events'))
    CHOICE3 = ((0,'Select:'),(1, 'First'),(2, 'Second'),(3, 'Third'))
    CHOICE4 = ((0,'Select:'), (1, '(a) Certificate'), (2, '(b) Letter from Authorities'),
               (3, '(c) Appreciation recognition letter'), (4, '(d)Documentary evidence'),
               (5, '(e) Legal Proof'), (6, 'Others')
               )

    user3 = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    OneYear = models.IntegerField(choices=CHOICE, default=0)
    Category = models.IntegerField(choices=CHOICE1, default=0)
    Level = models.IntegerField(choices=CHOICE2, default=0)
    Position = models.IntegerField(choices=CHOICE3, default=0)
    DocType = models.IntegerField(choices=CHOICE4, default=0)
    File = models.FileField(null=True, blank=True)
    Approved = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.user3)

class ProfPage(models.Model):
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

    user4 = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    Category = models.IntegerField(choices=CHOICE, default=0)
    Level = models.IntegerField(choices=CHOICE1, default=0)
    DocType = models.IntegerField(choices=CHOICE2, default=0)
    File = models.FileField(null=True, blank=True)
    Approved = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.user4)

class EntrePage(models.Model):
    CHOICE = ((0, 'Select:'),
               (1,'Start-up Company –Registered legally'),
               (2,'Patent-Filed'),
               (3,'Patent-Published'),
               (4,'Patent-Approved'),
               (5,'Patent-Licensed'),
               (6, 'Prototype developed and tested'),
               (7,'Awards for Products developed'),
               (8,'Innovative technologies developed and used by industries/users'),
               (9,'Got venture capital funding for innovative ideas/products'),
               (10, 'Startup Employment (Offering jobs to two persons less than Rs. 15000/- per month)'),
               (11, 'Societal innovations'))
    CHOICE1 = ((0, 'Select:'), (1, '(a) Certificate'), (2, '(b) Letter from Authorities'),
               (3, '(c) Appreciation recognition letter'), (4, '(d)Documentary evidence'),
               (5, '(e) Legal Proof'), (6, 'Others')
               )

    user5 = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    Category = models.IntegerField(choices=CHOICE, default=0)
    DocType = models.IntegerField(choices=CHOICE1, default=0)
    File = models.FileField(null=True, blank=True)
    Approved = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.user5)

class GamePage(models.Model):
    CHOICE = ((1, 'Yes'), (2, 'No'))
    CHOICE1 = ((0, 'Select:'), (1, 'Sports'), (2, 'Games'))
    CHOICE2 = ((0, 'Select:'), (1, 'College Events'), (2, 'Zonal Events'), (3, 'State/ University Events'),
               (4, 'National Events'), (5, 'International Events'))
    CHOICE3 = ((0, 'Select:'), (1, 'First'), (2, 'Second'), (3, 'Third'))
    CHOICE4 = ((0, 'Select:'), (1, '(a) Certificate'), (2, '(b) Letter from Authorities'),
               (3, '(c) Appreciation recognition letter'), (4, '(d)Documentary evidence'),
               (5, '(e) Legal Proof'), (6, 'Others')
               )

    user6 = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    OneYear = models.IntegerField(choices=CHOICE, default=0)
    Category = models.IntegerField(choices=CHOICE1, default=0)
    Level = models.IntegerField(choices=CHOICE2, default=0)
    Position = models.IntegerField(choices=CHOICE3, default=0)
    DocType = models.IntegerField(choices=CHOICE4, default=0)
    File = models.FileField(null=True, blank=True)
    Approved = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.user6)

class NatPage(models.Model):
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

    user2 = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    TwoYears = models.IntegerField(choices=CHOICE, default=0)
    Category = models.IntegerField(choices=CHOICE1, default=0)
    SubCategory = models.IntegerField(choices=CHOICE2, default=0)
    DocType = models.IntegerField(choices=CHOICE3, default=0)
    File = models.FileField(null=True, blank=True)
    Approved = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.user2)
