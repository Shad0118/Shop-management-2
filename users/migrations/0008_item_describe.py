# Generated by Django 4.1.2 on 2023-05-29 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_pname_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='describe',
            field=models.CharField(default='some String', max_length=100),
        ),
    ]
