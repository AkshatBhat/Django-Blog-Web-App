from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"{username}, your account has been created! You can now login with your credentials!")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    context = dict(form=form)
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile) 
        # request.FILES -> Because image is gonna be uploaded
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request,f"{username}, your account has been updated!")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request,'users/profile.html',context) 