from django.db import models
from django.conf import settings

class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=250)

    def __str__(self):
        return f'Profile {self.user.username}'