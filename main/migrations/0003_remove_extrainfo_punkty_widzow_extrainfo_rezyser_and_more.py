# Generated by Django 5.0.2 on 2024-03-12 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_aktor_extrainfo_ocena'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extrainfo',
            name='punkty_widzow',
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='rezyser',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Inne'), (4, 'Dramat'), (1, 'Horror'), (3, 'Sci-fi'), (2, 'Komedia')], null=True),
        ),
    ]
