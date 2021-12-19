from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    account_created = models.DateTimeField(default=timezone.now, blank=False, null=False)
    deposited = models.FloatField(null=False, blank=False, default=0)
    rating = models.FloatField(null=False, blank=False, default=0)

    def __str__(self):
        return self.user.username