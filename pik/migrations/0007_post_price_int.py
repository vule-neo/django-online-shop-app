# Generated by Django 3.0.3 on 2020-03-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pik', '0006_auto_20200323_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price_int',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
