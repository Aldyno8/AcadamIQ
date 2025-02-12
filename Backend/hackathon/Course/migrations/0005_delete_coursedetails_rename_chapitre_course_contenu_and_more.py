# Generated by Django 5.0.6 on 2024-07-01 05:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0004_coursedetails_rename_lesson_course_chapitre'),
        ('Positioning', '0004_remove_userscore_score_userscore_niveau'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CourseDetails',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='chapitre',
            new_name='Contenu',
        ),
        migrations.AlterField(
            model_name='course',
            name='niveau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Positioning.userscore'),
        ),
    ]
