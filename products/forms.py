from django import forms
from .models.Models_Product import Product
from .models.Models_Category import Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(**args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(category.id, category.friendly_name())
                          for category in categories]

        self.fields['category'].choices = friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'