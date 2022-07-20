from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models.Models_Profile import UserProfile
from .forms import UserProfileForm


@login_required(login_url='/auth/login')
def profile(request):
    """
    Display the user's profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
        else:
            messages.error(
                request,
                'Something went wrong while trying to update your profile. '
                'Please try again later.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()
    context = {
        'form': form,
        'on_profile_page': True,
    }
    return render(request, 'profiles/profile.html', context=context)