# Generated by Django 3.1 on 2020-08-07 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0011_person_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='acronym',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
