from django.shortcuts import render,redirect
from .forms  import MembersRegisterForm
from django.contrib  import messages
from django.http   import HttpResponse,HttpResponseBadRequest
from django.contrib.auth   import login,logout,authenticate
from django.urls    import reverse_lazy

def register_member(request):
    if request.method == 'POST':
        form = MembersRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request,'your request is submitted successfully!')
            return HttpResponse('Your request is submitted successfully!')
        else:
            return HttpResponseBadRequest('bad')
    else:
        form = MembersRegisterForm()
    return render(request,'accounts/reg.html',{'form':form})

def login_member(request):
    if request.method == 'POST':
        email = request.POST['login-email']
        password = request.POST['login-password']
        user = authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            message = 'Logged in Successful'
        else:
            message = 'Error Trying To Log In.'
        return render(request,'accounts/login.html',{'message':message})

   
    return render(request,'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')
