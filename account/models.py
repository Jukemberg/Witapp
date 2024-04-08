from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    personal_number = models.CharField(max_length=13, blank=True, null=True)
    work_number = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
