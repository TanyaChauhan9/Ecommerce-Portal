# Generated by Django 2.1.5 on 2019-01-20 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webgen', '0004_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='user',
            new_name='use',
        ),
    ]