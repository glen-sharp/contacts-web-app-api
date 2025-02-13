# Generated by Django 5.1.6 on 2025-02-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='forename',
        ),
        migrations.AddField(
            model_name='contact',
            name='surname',
            field=models.CharField(default=None, max_length=120),
            preserve_default=False,
        ),
    ]
