from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserRegistrationForm() # empty form
    return render(request,'user/register.html',{'form':form})


def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(request.FILES,instance = request.user.profile)
    
    return render(request,'user/profile.html',{'u_form':u_form,'p_form':p_form})