from django.contrib import admin
from .models.Models_Newsletter import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'user_email',
        'created_at'
    )
    search_fields = ('user_email',)

admin.site.register(Newsletter, NewsletterAdmin)