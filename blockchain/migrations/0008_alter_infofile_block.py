# Generated by Django 3.2.6 on 2021-08-13 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0007_infofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infofile',
            name='block',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='infofile', to='blockchain.block'),
        ),
    ]