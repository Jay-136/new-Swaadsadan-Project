# Generated by Django 4.0 on 2022-04-06 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0012_southjproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Punjabijproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('img', models.ImageField(null=True, upload_to='pics')),
                ('desc', models.TextField(max_length=100, null=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
    ]
