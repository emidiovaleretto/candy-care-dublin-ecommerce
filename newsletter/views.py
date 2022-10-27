from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models.Models_Newsletter import Newsletter
from .forms import NewsletterForm


def newsletter(request):
    """
    This method handles the newsletter subscription
    and save the user email in database
    """
    form = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            if Newsletter.objects.filter(user_email=instance.user_email).exists():
                messages.info(
                    request, 'This email address is already subscribed.')
                return redirect(reverse('home'))
            else:
                instance.save()
                return redirect(reverse('success'))

    context = {
        'form': form
    }

    return render(request, 'home/index.html', context=context)
