# Generated by Django 3.1 on 2020-08-11 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0025_auto_20200807_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partyaffiliation',
            name='person',
        ),
        migrations.RemoveField(
            model_name='partyaffiliation',
            name='political_party',
        ),
        migrations.RemoveField(
            model_name='partyaffiliation',
            name='status',
        ),
        migrations.RemoveField(
            model_name='partydetail',
            name='party',
        ),
        migrations.AlterField(
            model_name='event',
            name='tagged_institutions',
            field=models.ManyToManyField(blank=True, related_name='tagged_events', to='story.Institution'),
        ),
        migrations.DeleteModel(
            name='OldPoliticalParty',
        ),
        migrations.DeleteModel(
            name='PartyAffiliation',
        ),
        migrations.DeleteModel(
            name='PartyDetail',
        ),
    ]
