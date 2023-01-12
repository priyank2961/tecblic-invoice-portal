# Generated by Django 4.0.4 on 2022-07-05 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecblicapp', '0059_remove_invoice_slug_remove_invoice_uniqueid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='cost_per_unit',
            new_name='cost_per_unit1',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='quantity',
            new_name='quantity1',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='description',
        ),
        migrations.AddField(
            model_name='invoice',
            name='cost_per_unit2',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='cost_per_unit3',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='description1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='description2',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='description3',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='quantity2',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='quantity3',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Online', 'Online'), ('Cheque', 'Cheque'), ('Swift Transfer', 'Swift Transfer')], default='CASH', max_length=100),
        ),
    ]