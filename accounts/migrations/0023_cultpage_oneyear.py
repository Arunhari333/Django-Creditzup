# Generated by Django 2.0.3 on 2018-08-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_natpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultpage',
            name='OneYear',
            field=models.IntegerField(choices=[(1, 'Yes'), (2, 'No')], default=0),
        ),
    ]