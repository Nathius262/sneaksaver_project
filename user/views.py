from django.shortcuts import render
from .models import Profile
from authentication.models import CustomUser
from .forms import AccountSettingsForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.
def account_setting_view(request):
    
    if request.POST:
        
        form = AccountSettingsForm(request.POST or None, request.FILES or None, instance=request.user)

        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
                "first_name": request.POST['first_name'],
                "last_name": request.POST['last_name'],
                "image": request.user.user_profile.image_url
            }
            
            form.save(commit=True)
            
        else:
            form = AccountSettingsForm(
                initial={
                    "email": request.user.email,
                    "username": request.user.username,
                    "first_name": request.user.user_profile.first_name,
                    "last_name": request.user.user_profile.last_name,
                    "image": request.user.user_profile.image_url
                }
            )
        
    else:
        try:
            form = AccountSettingsForm(
                initial={
                    "email": request.user.email,
                    "username": request.user.username,
                    "first_name": request.user.user_profile.first_name,
                    "last_name": request.user.user_profile.last_name,
                    "image": request.user.user_profile.image_url
                }
            )
        except ObjectDoesNotExist:
            pass 
    context = {
        'form': form,
    }
    return render(request, 'user/account.html', context)