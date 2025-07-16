from django.contrib.auth.forms   import UserCreationForm,UserChangeForm
from django.contrib.auth.models  import User
from .models  import ShisMemberUser
from django    import forms
class MembersRegisterForm(UserCreationForm):

    class Meta:
        model = ShisMemberUser
        fields = ['first_name','last_name','nick_name','photo','email','phone','graduation_year']
        widgets = {
            'graduation_year': forms.DateInput(attrs={'type':'date'}),
            'phone': forms.NumberInput(attrs={'type':'tel'}),
        }

class MembersChangeform(UserChangeForm):
    class Meta:
        model = ShisMemberUser
        fields = ['first_name','last_name','nick_name','photo','email','phone','graduation_year','status']
        widgets = {
            'graduation_year': forms.DateInput(attrs={'type':'date'}),
            'phone': forms.NumberInput(attrs={'type':'tel'}),
        }