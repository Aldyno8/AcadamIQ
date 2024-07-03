# Generated by Django 5.0.6 on 2024-06-21 23:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapitre', models.TextField()),
                ('niveau', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='coursedetail',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.course'),
        ),
    ]
