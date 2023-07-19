# Generated by Django 4.2.3 on 2023-07-18 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_asset_hdd_asset_invoice_asset_processor_asset_ram_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='attachements/')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.asset')),
            ],
        ),
    ]
