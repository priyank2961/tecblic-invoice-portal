# Generated by Django 4.0.4 on 2022-05-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecblicapp', '0011_clientdetail_placeofsupply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='id',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_no',
            field=models.IntegerField(default=500, primary_key=True, serialize=False),
        ),
    ]