# Generated by Django 2.1.7 on 2019-05-18 06:59

from django.db import migrations
import ool


class Migration(migrations.Migration):

    dependencies = [
        ('rssant_api', '0008_auto_20190429_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='_version',
            field=ool.VersionField(default=0),
        ),
        migrations.AddField(
            model_name='feedurlmap',
            name='_version',
            field=ool.VersionField(default=0),
        ),
        migrations.AddField(
            model_name='rawfeed',
            name='_version',
            field=ool.VersionField(default=0),
        ),
        migrations.AddField(
            model_name='story',
            name='_version',
            field=ool.VersionField(default=0),
        ),
        migrations.AddField(
            model_name='userfeed',
            name='_version',
            field=ool.VersionField(default=0),
        ),
        migrations.AddField(
            model_name='userstory',
            name='_version',
            field=ool.VersionField(default=0),
        ),
    ]
