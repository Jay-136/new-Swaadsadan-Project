# Generated by Django 4.0 on 2022-04-29 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0029_category_banner_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='banner_img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
