# Generated by Django 3.1 on 2020-08-07 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0015_auto_20200807_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticalParty',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('story.institution',),
        ),
    ]