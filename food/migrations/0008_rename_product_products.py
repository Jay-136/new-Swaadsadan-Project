# Generated by Django 4.0 on 2022-04-05 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_remove_product_category_remove_product_desc_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Products',
        ),
    ]
