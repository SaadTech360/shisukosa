from django.urls  import path
from .views    import register_member,login_member,logout_user

app_name = 'accounts'
urlpatterns = [
  path('register/',register_member,name='register'),
  path('login/',login_member,name='login'),
  path('logout/',logout_user,name='logout'),

]