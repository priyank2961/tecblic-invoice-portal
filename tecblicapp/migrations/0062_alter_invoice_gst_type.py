# Generated by Django 4.0.4 on 2022-08-08 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecblicapp', '0061_alter_invoice_cost_per_unit1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='gst_type',
            field=models.CharField(choices=[('DOMESTIC', 'DOMESTIC'), ('EXPORT', 'EXPORT'), ('Inter State', 'Inter State')], default='DOMESTIC', max_length=20),
        ),
    ]
