# Generated by Django 4.0 on 2022-05-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0030_alter_category_banner_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
