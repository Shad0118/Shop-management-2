# Generated by Django 4.1.2 on 2023-05-29 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_name_item_pname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='pname',
            new_name='name',
        ),
    ]