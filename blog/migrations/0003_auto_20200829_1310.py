# Generated by Django 2.2.15 on 2020-08-29 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approved_comment',
            new_name='hide_comment',
        ),
    ]