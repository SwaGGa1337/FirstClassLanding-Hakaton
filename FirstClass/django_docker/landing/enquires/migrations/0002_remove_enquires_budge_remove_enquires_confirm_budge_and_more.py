# Generated by Django 5.0.3 on 2024-04-17 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquires', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquires',
            name='budge',
        ),
        migrations.RemoveField(
            model_name='enquires',
            name='confirm_budge',
        ),
        migrations.RemoveField(
            model_name='enquires',
            name='continent',
        ),
        migrations.RemoveField(
            model_name='enquires',
            name='created',
        ),
        migrations.RemoveField(
            model_name='enquires',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='enquires',
            name='email',
        ),
        migrations.RemoveField(
            model_name='enquires',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='enquires',
            name='num_of_travelers',
        ),
        migrations.RemoveField(
            model_name='enquires',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='enquires',
            name='sub_for_contact',
        ),
        migrations.RemoveField(
            model_name='enquires',
            name='text',
        ),
        migrations.RemoveField(
            model_name='enquires',
            name='trip_type',
        ),
    ]