from django.shortcuts import render,redirect,get_object_or_404
from accounts.models  import ShisMemberUser
from accounts.forms   import MembersRegisterForm
from django.contrib.auth.decorators  import login_required
from django.http   import HttpResponseForbidden
from .forms   import EventsCreationForm,GalleryUploadForm
from .models   import Events,Gallery
from django.contrib    import messages

def homepage(request):
    admins = ShisMemberUser.objects.filter(is_staff=True)[:3]
    return render(request,'members/home.html',{'admins':admins})

def members_list(request):
    members = ShisMemberUser.objects.all()
    return render(request,'members/member-list.html',{'members':members})

def membership_request_list(request):
    return render(request,'members/membership_request.html')

def membership_request_detail(request):
    return render(request,'members/membership_detail.html')

@login_required
def create_admin_user(request):
    if request.method == 'POST':
        form = MembersRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.status = 'APPROVED'

            user.save()
             
            message = 'Admin Added Successfully'

        else:
            message = 'Your Input is Invalid, pls check.'
        return render(request,'members/add_admin.html',{'form':form,'message':message})
    else:
        form = MembersRegisterForm()
    return render(request,'members/add_admin.html',{'form':form})

@login_required
def accept_member(request,pk):
    pending_member = get_object_or_404(ShisMemberUser,pk=pk)
    if pending_member.status == 'PENDING':
        pending_member.status = 'APPROVED'
        pending_member.save()
        # message = 'User Accepted'
        return redirect('/dashboard/')
def delete_members(request,pk):
    member = get_object_or_404(ShisMemberUser,pk=pk)
    member.delete()
    return redirect('/dashbord/')

@login_required(login_url='/login/')
def admin_dashboard(request):
    if request.user.is_staff:
        pending_requests = ShisMemberUser.objects.filter(status='PENDING').count()
        active_members = ShisMemberUser.objects.filter(status='APPROVED').count()
        membership_request = ShisMemberUser.objects.filter(status='PENDING').exclude(is_staff=True)[:10]
        contexts = {'membership_request':membership_request,
                    'active_members':active_members,'pending_requests':pending_requests}
        return render(request,'members/dashboard.html',contexts)
    else:
        return HttpResponseForbidden('Only Admins are Allow to Access This Side')
    
def event(request):
    events = Events.objects.all()
    past_events = Events.objects.filter(status='DONE')
    return render(request,'members/events.html',{'events':events,'past_events':past_events})
@login_required
def create_event(request):
    if request.user.is_staff and request.method == 'POST':
        form = EventsCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            message = ' Event Created Successfully.'
        else:
            message = ' Error while creating Event.'
        return render(request,'members/create_event.html',{'form':form,'message':message})
    elif not request.user.is_staff:
        return HttpResponseForbidden('Only admin is allow to Create Events.')
    else:
        form = EventsCreationForm()
    return render(request,'members/create_event.html',{'form':form})

@login_required
def edit_event(request,pk):
    event = get_object_or_404(Events,pk=pk)
    form  = EventsCreationForm(instance=event)
    return render(request,'members/edit_event.html',{'form':form})

@login_required
def delete_event(request,pk):
    event = get_object_or_404(Events,pk=pk)
    event.delete()
    return redirect('/events/')

def event_detail(request,pk):
    event = get_object_or_404(Events,pk=pk)
    return render(request,'members/event_detail.html',{'event':event})
    
def gallery(request):
    pictures = Gallery.objects.all()
    return render(request,'members/gallery.html',{'pictures':pictures})

@login_required
def gallery_upload(request):
    if request.method == 'POST' and request.user.is_staff:
        form = GalleryUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Gallery Uploaded Successfully')
        else:
            messages.error(request,'Error While Uploading.')
    elif not request.user.is_staff:
        return HttpResponseForbidden('ONLY Admins Are Allow to Upload to Gallery.')
    else:
        form = GalleryUploadForm()

    return render(request,'members/gallery_upload.html',{'form':form})

@login_required
def edit_gallery(request,pk):
    gallery = get_object_or_404(Gallery,pk=pk)
    form = GalleryUploadForm(instance=gallery)
    return render(request,'members/edit_gallery.html',{'form':form})

@login_required
def delete_gallery(request,pk):
    gallery = get_object_or_404(Gallery,pk=pk)
    gallery.delete()
    return redirect('/gallery/')