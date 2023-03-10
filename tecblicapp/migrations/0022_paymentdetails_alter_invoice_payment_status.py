# Generated by Django 4.0.4 on 2022-05-06 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tecblicapp', '0021_alter_invoice_payment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='paymentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_s', models.CharField(choices=[('PENDING', 'PENDING'), ('PAID', 'PAID')], default='PENDING', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_status',
            field=models.ForeignKey(default='PENDING', max_length=100, on_delete=django.db.models.deletion.CASCADE, to='tecblicapp.paymentdetails'),
        ),
    ]
