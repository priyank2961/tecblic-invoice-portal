# Generated by Django 4.0.4 on 2022-05-03 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecblicapp', '0009_clientdetail_kindattn_alter_invoice_send_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]