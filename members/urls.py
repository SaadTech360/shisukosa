from django.urls  import path
from .views   import (homepage,members_list,create_admin_user,admin_dashboard,
   accept_member,delete_members,event,create_event,gallery,membership_request_list,
   membership_request_detail,event_detail,gallery_upload,edit_gallery,delete_gallery,edit_event,
   delete_event)

app_name = 'members'
urlpatterns = [
   path('',homepage,name='home'),
   path('members/',members_list,name='members_list'),
   path('create-admin/',create_admin_user, name='add_admin'),
   path('dashboard/',admin_dashboard,name='dashboard'),
   path('accept-member/<int:pk>/',accept_member,name='accept'),
   path('delete/<int:pk>/',delete_members,name='delete'),
   path('events/',event,name='events'),
   path('create-event/',create_event,name='create_event'),
   path('edit-event/<int:pk>/',edit_event,name='edit_even'),
   path('delete-event/<int:pk>/',delete_event,name='delete_event'),
   path('event/<int:pk>/',event_detail,name='event_detail'),
   path('gallery/',gallery,name='gallery'),
   path('upload-gallery/',gallery_upload,name='gallery_upload'),
   path('edit-gallery/<int:pk>/',edit_gallery,name='gallery_upload'),
   path('delete-gallery/<int:pk>/',delete_gallery,name='delete_gallery'),
   path('membership-request-lists/',membership_request_list,name='membership_request_list'),
   path('membership-request-detail/',membership_request_detail,name='membership_request_detail'),
]