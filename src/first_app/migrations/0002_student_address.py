# Generated by Django 2.2.9 on 2020-01-08 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]