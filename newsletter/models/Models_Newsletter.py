from django.db import models


class Newsletter(models.Model):
    """ A model to create a newsletter subscription"""
    
    user_email = models.EmailField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_email
    