# Generated by Django 4.1.2 on 2023-05-29 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_item_describe'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='brandname',
            field=models.CharField(default='Pran', max_length=30),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.CharField(default='50', max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='describe',
            field=models.CharField(default='String', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default='Juice', max_length=100),
        ),
    ]
