# Generated by Django 3.2 on 2022-07-12 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20220712_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inrprotocolprofile',
            name='inr_range',
        ),
        migrations.AddField(
            model_name='inrrangeprofile',
            name='inr_protocol',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='inrprotocal_profile', to='userprofile.inrprotocolprofile'),
        ),
    ]