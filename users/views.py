from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm,UserUpdateForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account created successfully for {username}.")
            return redirect('user-login')

    else:
        form = UserRegisterForm()

    return render(request,'users/register.html',{
        'form':form
    })


def logout_user(request):
    if request.user.is_authenticated:
        messages.success(request,f"You have logged out!")
    else:
        messages.error(request,f"You must login before logging out!",extra_tags='danger')

    logout(request)
    return redirect('user-login')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request,f"Profile Updated!")
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form,
    }

    return render(request,'users/profile.html',context)

def edit_profile(request):
    pass