# Generated by Django 4.0.4 on 2022-05-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecblicapp', '0010_invoice_description_invoice_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdetail',
            name='placeofSupply',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
