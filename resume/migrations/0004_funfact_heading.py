# Generated by Django 3.2.18 on 2023-03-22 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_rename_background_image_aboutme_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='funfact',
            name='heading',
            field=models.CharField(default='Clients Happy', max_length=29),
            preserve_default=False,
        ),
    ]
