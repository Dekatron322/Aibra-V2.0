# Generated by Django 4.1.3 on 2022-12-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_remove_job_skill_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='website',
            field=models.CharField(default='none', max_length=30),
        ),
        migrations.AddField(
            model_name='jobrequest',
            name='address',
            field=models.CharField(default='none', max_length=30),
        ),
        migrations.AddField(
            model_name='jobrequest',
            name='category',
            field=models.CharField(default='none', max_length=30),
        ),
        migrations.AddField(
            model_name='jobrequest',
            name='experience',
            field=models.CharField(default='none', max_length=120),
        ),
        migrations.AddField(
            model_name='jobrequest',
            name='website',
            field=models.CharField(default='none', max_length=30),
        ),
    ]
