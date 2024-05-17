# Generated by Django 4.0 on 2022-04-14 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('food', '0017_category_product_delete_chinesseproduct_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
