from django.contrib.auth.forms   import UserCreationForm,UserChangeForm
from django.contrib.auth.models  import User
from .models  import ShisMemberUser

class MembersRegisterForm(UserCreationForm):

    class Meta:
        model = ShisMemberUser
        fields = ['first_name','last_name','nick_name','photo','email','phone','graduation_year']

class MembersChangeform(UserChangeForm):
    class Meta:
        model = ShisMemberUser
        fields = ['first_name','last_name','nick_name','photo','email','phone','graduation_year','status']