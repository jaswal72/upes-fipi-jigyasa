# Generated by Django 2.1.7 on 2019-03-23 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190324_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='referral',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='REFERRAL'),
        ),
    ]
