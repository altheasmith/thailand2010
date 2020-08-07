# Generated by Django 3.1 on 2020-08-07 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0016_politicalparty'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='politicalparty',
            options={'verbose_name_plural': 'Political parties'},
        ),
        migrations.AddField(
            model_name='institutiondetail',
            name='tagged_events',
            field=models.ManyToManyField(blank=True, to='story.Event'),
        ),
        migrations.AddField(
            model_name='institutiondetail',
            name='tagged_institutions',
            field=models.ManyToManyField(blank=True, to='story.Institution'),
        ),
        migrations.AddField(
            model_name='institutiondetail',
            name='tagged_persons',
            field=models.ManyToManyField(blank=True, to='story.Person'),
        ),
        migrations.AddField(
            model_name='persondetail',
            name='tagged_events',
            field=models.ManyToManyField(blank=True, to='story.Event'),
        ),
        migrations.AddField(
            model_name='persondetail',
            name='tagged_institutions',
            field=models.ManyToManyField(blank=True, to='story.Institution'),
        ),
        migrations.AddField(
            model_name='persondetail',
            name='tagged_persons',
            field=models.ManyToManyField(blank=True, to='story.Person'),
        ),
        migrations.AlterField(
            model_name='institutiondetail',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='story.institution'),
        ),
        migrations.AlterField(
            model_name='persondetail',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='story.person'),
        ),
    ]