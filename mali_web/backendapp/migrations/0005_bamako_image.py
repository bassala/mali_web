# Generated by Django 5.0.3 on 2024-05-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0004_remove_region_habitats'),
    ]

    operations = [
        migrations.AddField(
            model_name='bamako',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]