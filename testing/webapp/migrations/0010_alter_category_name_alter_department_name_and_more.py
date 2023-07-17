# Generated by Django 4.2.3 on 2023-07-17 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_status_asset_checkout_status_alter_asset_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Type of asset', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(help_text='Name of department', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(help_text='Name of manufacturing company', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(help_text='Status of asset', max_length=200, unique=True),
        ),
    ]
