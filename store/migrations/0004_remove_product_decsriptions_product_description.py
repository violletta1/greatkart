# Generated by Django 5.0.6 on 2024-06-05 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_productgallery_reviewrating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='decsriptions',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
