# Generated by Django 5.1.4 on 2025-07-15 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_shismemberuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='shismemberuser',
            name='photo',
            field=models.ImageField(default='profiles/student.png', upload_to='profiles/img'),
        ),
    ]
