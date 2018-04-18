# Generated by Django 2.0.4 on 2018-04-18 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='profile_pic_id',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='profile_pic_url',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
