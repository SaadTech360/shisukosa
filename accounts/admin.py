from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models  import ShisMemberUser
from .forms   import MembersRegisterForm,MembersChangeform

class MemberUserAdmin(UserAdmin):
    list_display = ['first_name','last_name','email','graduation_year','phone','is_staff']
    ordering = ['graduation_year']
    search_fields = ['email','nick_name','graduation_year']
    list_filter = ['email','graduation_year','status']
    add_form = MembersRegisterForm
    form = MembersChangeform
    fieldsets = (
        (None,{'fields':('email','password')}),
    ('Personal Info',{'fields':('first_name','last_name','phone','graduation_year','status')}),
    )
    add_fieldsets = (
        ('Info',{'classes':('wide',),'fields':('first_name','last_name','phone','graduation_year','password1','password2')}),
    )
    






admin.site.register(ShisMemberUser,MemberUserAdmin)
