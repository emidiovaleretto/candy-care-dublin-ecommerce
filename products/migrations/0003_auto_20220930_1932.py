# Generated by Django 3.2 on 2022-09-30 18:32

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220923_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
