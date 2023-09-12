# Generated by Django 4.0.1 on 2023-07-30 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0005_auto_20210512_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quesmodel',
            name='id',
        ),
        migrations.AddField(
            model_name='quesmodel',
            name='Img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='quesmodel',
            name='question',
            field=models.CharField(max_length=200, primary_key='true', serialize=False),
        ),
    ]
