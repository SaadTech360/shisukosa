# Generated by Django 5.1.4 on 2025-07-16 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_shismemberuser_fb_link_shismemberuser_ig_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shismemberuser',
            old_name='fb_link',
            new_name='social_link',
        ),
        migrations.RemoveField(
            model_name='shismemberuser',
            name='ig_link',
        ),
        migrations.RemoveField(
            model_name='shismemberuser',
            name='x_link',
        ),
    ]
