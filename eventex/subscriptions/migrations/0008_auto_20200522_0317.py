# Generated by Django 2.2.12 on 2020-05-22 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0007_auto_20200522_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='hash_url',
            field=models.CharField(max_length=32, null=True, verbose_name='URL'),
        ),
    ]
