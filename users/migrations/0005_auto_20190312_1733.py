# Generated by Django 2.1.7 on 2019-03-12 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190312_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='contact_no',
            field=models.BigIntegerField(default=91),
        ),
        migrations.AddField(
            model_name='user_details',
            name='status',
            field=models.CharField(default='Not Paid', max_length=12, verbose_name='STATUS'),
        ),
    ]
