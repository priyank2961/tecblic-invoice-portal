# Generated by Django 4.0.4 on 2022-05-31 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecblicapp', '0054_savepdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savepdf',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]