# Generated by Django 4.0.1 on 2023-07-30 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0007_remove_quesmodel_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('classification', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_year', models.CharField(max_length=10)),
                ('eye_color', models.CharField(max_length=10)),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Quiz.species')),
            ],
        ),
    ]
