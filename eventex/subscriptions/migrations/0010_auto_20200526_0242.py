# Generated by Django 2.2.12 on 2020-05-26 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0009_auto_20200525_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='hash_url',
            field=models.UUIDField(default='97e76fcc9efa11ea8dc47085c207b2ef'),
        ),
    ]