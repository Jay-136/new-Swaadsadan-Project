# Generated by Django 4.0 on 2022-04-06 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_rename_product_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
