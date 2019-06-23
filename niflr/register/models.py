#from __future__ import unicode_literals


from django.contrib.auth.models import Permission, User
from django.db import models

class UserProfil(User):
    mobile_number = models.PositiveIntegerField(blank=True)
    firstname = models.CharField(max_length=300, blank=False)
    lastname = models.CharField(max_length=300,  blank=False)
    birthdate = models.DateField(blank=True)
	
    
