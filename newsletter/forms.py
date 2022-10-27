from django import forms
from .models.Models_Newsletter import Newsletter


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = ('user_email',)
