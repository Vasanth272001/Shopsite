# Generated by Django 4.2.6 on 2023-10-25 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_catagory_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Catagory',
        ),
    ]
