# Generated by Django 3.0.3 on 2020-02-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voteoption',
            name='vote_num',
            field=models.IntegerField(default=0),
        ),
    ]
