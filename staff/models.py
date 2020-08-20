from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StaffProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    FirstName = models.CharField(max_length=100, default='')
    LastName = models.CharField(max_length=100, default='')
    Class = models.CharField(max_length=100, default='')
    Semester = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % self.user
