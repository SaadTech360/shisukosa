from django.shortcuts import render,redirect,get_object_or_404
from accounts.models  import ShisMemberUser
from accounts.forms   import MembersRegisterForm
from django.contrib.auth.decorators  import login_required
from django.http   import HttpResponseForbidden
from .forms   import EventsCreationForm

def homepage(request):
    return render(request,'members/home.html')

def members_list(request):
    members = ShisMemberUser.objects.all()
    return render(request,'members/member-list.html',{'members':members})

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
    return render(request,'members/events.html')

def create_event(request):
    if request.user.is_staff and request.method == 'POST':
        form = EventsCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            message = ' Event Created Successfully.'
        else:
            message = ' Event Created Successfully.'
        return render(request,'members/create_event.html',{'form':form,'message':message})
    elif not request.user.is_staff:
        return HttpResponseForbidden('Only admin is allow to Create Events.')
    else:
        form = EventsCreationForm()
    return render(request,'members/create_event.html',{'form':form})

    
    
def gallery(request):
    return render(request,'members/gallery.html')