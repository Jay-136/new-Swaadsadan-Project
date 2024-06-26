# Generated by Django 4.0 on 2022-04-14 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('food', '0018_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250)),
                ('product_price', models.FloatField()),
                ('product_img', models.ImageField(upload_to='pics')),
                ('details', models.TextField()),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
