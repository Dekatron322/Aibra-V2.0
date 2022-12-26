# Generated by Django 4.1.3 on 2022-11-24 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='city',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='current_salary',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='discord_link',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='expected_salary',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='state',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='facebook_link',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='github_link',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='instagram_link',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='linkedin_link',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='twitter_link',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
