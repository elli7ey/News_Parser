# Generated by Django 3.0.8 on 2020-07-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]