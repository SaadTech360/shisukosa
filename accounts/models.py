from django.db import models
from django.contrib.auth.models  import AbstractUser
from .managers  import ShisMemberManager


class ShisMemberUser(AbstractUser):
    MEMBER_STATUS = [
        ('APPROVED','approve'),
        ('PENDING','pending')
    ]
    username = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    email  = models.EmailField(unique=True)
    phone = models.IntegerField(null=True,blank=True)
    graduation_year = models.DateField(editable=True)
    status = models.CharField(choices=MEMBER_STATUS,default='PENDING',max_length=50)
    request_date = models.DateTimeField(auto_now_add=True)
    approved_date = models.DateTimeField(auto_now=True)

    objects = ShisMemberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','graduation_year']

    def __str__(self):
        return f'{self.first_name} {self.last_name} [ {self.email} ]'

