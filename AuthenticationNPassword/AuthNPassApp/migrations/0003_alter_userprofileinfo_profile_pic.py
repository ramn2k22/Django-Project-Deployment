# Generated by Django 4.2.5 on 2023-10-14 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthNPassApp', '0002_rename_portfolia_site_userprofileinfo_portfolio_site_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pic'),
        ),
    ]