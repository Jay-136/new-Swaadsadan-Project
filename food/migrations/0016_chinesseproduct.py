# Generated by Django 4.0 on 2022-04-06 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0015_indianstreetproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chinesseproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('img', models.ImageField(null=True, upload_to='pics')),
                ('desc', models.TextField(max_length=100, null=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
    ]
