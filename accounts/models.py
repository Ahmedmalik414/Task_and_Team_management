from django.contrib.auth.models import AbstractUser
from django.db import models

SENIORITY_CHOICES = [
    ("junior", "Junior"),
    ("mid", "Mid-level"),
    ("senior", "Senior"),
    ("lead", "Lead"),
]

class CustomUser(AbstractUser):
    seniority = models.CharField(
        max_length=10,  
        choices=SENIORITY_CHOICES,
        default="junior"  
    )
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.username