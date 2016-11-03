from django.db import models
from django.conf import settings
from datetime import datetime
from django.core.urlresolvers import reverse
# Create your models here.


User = settings.AUTH_USER_MODEL

GENDER_CHOICES = (('M', 'Male'),
                  ('F', 'Female'),
                  ('N', 'Not Disclosed'))


def upload_location(instance, filename):
    return '%s, %s' %(instance.first_name, filename)


class MasterProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=80, default='abc')
    last_name = models.CharField(max_length=80, default='abc')
    email = models.EmailField()
    phone = models.IntegerField()
    photo = models.ImageField(upload_to=upload_location, blank=True, null=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('master_detail', kwargs={'pk': self.pk})


class ParticipantProfile(models.Model):
    first_name = models.CharField(max_length=80, default='abc')
    last_name = models.CharField(max_length=80, default='abc')
    email = models.EmailField()
    phone = models.IntegerField()
    photo = models.ImageField(upload_to=upload_location, blank=True, null=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.email)

    def get_absolute_url(self):
        return reverse('member_detail', kwargs={'pk': self.pk})

