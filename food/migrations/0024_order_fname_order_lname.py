# Generated by Django 4.0 on 2022-04-22 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0023_remove_order_fname_remove_order_lname'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='fname',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='lname',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
