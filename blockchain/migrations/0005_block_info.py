# Generated by Django 3.2.6 on 2021-08-13 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0004_alter_infofile_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='info',
            field=models.BinaryField(null=True),
        ),
    ]
