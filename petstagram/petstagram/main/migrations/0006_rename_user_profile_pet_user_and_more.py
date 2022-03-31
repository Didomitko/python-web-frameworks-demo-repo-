# Generated by Django 4.0.2 on 2022-03-14 18:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_alter_pet_user_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='user_profile',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='pet',
            unique_together={('user', 'name')},
        ),
    ]