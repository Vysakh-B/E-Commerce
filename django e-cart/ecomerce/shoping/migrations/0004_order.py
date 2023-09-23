# Generated by Django 4.2.3 on 2023-07-31 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoping', '0003_alter_cart_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=20)),
                ('postal', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('products', models.CharField(max_length=200)),
                ('total', models.IntegerField()),
                ('payment', models.CharField(max_length=20)),
            ],
        ),
    ]