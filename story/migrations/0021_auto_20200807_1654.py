# Generated by Django 3.1 on 2020-08-07 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0020_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institutiondetail',
            name='tagged_events',
            field=models.ManyToManyField(blank=True, related_name='tagged_institution_details', to='story.Event'),
        ),
        migrations.AlterField(
            model_name='institutiondetail',
            name='tagged_institutions',
            field=models.ManyToManyField(blank=True, related_name='tagged_institution_details', to='story.Institution'),
        ),
        migrations.AlterField(
            model_name='institutiondetail',
            name='tagged_persons',
            field=models.ManyToManyField(blank=True, related_name='tagged_institution_details', to='story.Person'),
        ),
        migrations.AlterField(
            model_name='persondetail',
            name='tagged_events',
            field=models.ManyToManyField(blank=True, related_name='tagged_person_details', to='story.Event'),
        ),
        migrations.AlterField(
            model_name='persondetail',
            name='tagged_institutions',
            field=models.ManyToManyField(blank=True, related_name='tagged_person_details', to='story.Institution'),
        ),
        migrations.AlterField(
            model_name='persondetail',
            name='tagged_persons',
            field=models.ManyToManyField(blank=True, related_name='tagged_person_details', to='story.Person'),
        ),
    ]
