from django.db import models


class Occasion(models.Model):
    """
    This class creates a occasion
    e.g. mothers_day, christmas
    """

    class Meta:
        verbose_name_plural = 'Occasions'

    name = models.CharField(max_length=60)
    friendly_name = models.CharField(max_length=80, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        This method when called returns readable occasion name.
        """
        return self.name

    def get_friendly_name(self):
        """
        This method when called returns the friendly name of the occasion.
        e.g. Mother's Day, Christmas
        """
        return self.friendly_name
