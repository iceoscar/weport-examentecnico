# Generated by Django 4.2.4 on 2023-09-04 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergency_contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergencycontact',
            name='priority',
            field=models.PositiveSmallIntegerField(default=1, help_text='1 es mayor prioridad', verbose_name='Prioridad'),
        ),
    ]