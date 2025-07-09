from django.contrib.auth.base_user  import BaseUserManager

class ShisMemberManager(BaseUserManager):
    """ custom user model where email is the unique identifier"""
    def create_user(self,email,password,**extra_fields):
        """ create and save user with email and password"""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
    
    def create_superuser(self,email,password,**extra_fields):
        """create a superuser(admin)"""
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(' a superuser must be a staff')
        return self.create_user(email,password,**extra_fields)