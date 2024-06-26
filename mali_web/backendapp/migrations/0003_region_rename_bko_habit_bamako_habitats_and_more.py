# Generated by Django 5.0.3 on 2024-05-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0002_kayes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('habitats', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='bamako',
            old_name='Bko_habit',
            new_name='habitats',
        ),
        migrations.RenameField(
            model_name='gao',
            old_name='Gao_habit',
            new_name='habitats',
        ),
        migrations.RenameField(
            model_name='kayes',
            old_name='Kayes_habit',
            new_name='habitats',
        ),
        migrations.RenameField(
            model_name='kidal',
            old_name='Kidal_habit',
            new_name='habitats',
        ),
        migrations.RenameField(
            model_name='koulikoro',
            old_name='Koulikoro_habit',
            new_name='habitats',
        ),
        migrations.RenameField(
            model_name='mopti',
            old_name='Mopti_habit',
            new_name='habitats',
        ),
        migrations.RenameField(
            model_name='sikasso',
            old_name='Sikasso_habit',
            new_name='habitats',
        ),
        migrations.RenameField(
            model_name='ségou',
            old_name='Ségou_habit',
            new_name='habitats',
        ),
        migrations.RenameField(
            model_name='timbuktu',
            old_name='Timbuktu_habit',
            new_name='habitats',
        ),
    ]
