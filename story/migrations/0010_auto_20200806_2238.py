# Generated by Django 3.1 on 2020-08-06 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0009_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institutionaffiliation',
            name='title',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='partyaffiliation',
            name='title',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
