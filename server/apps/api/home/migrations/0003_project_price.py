# Generated by Django 4.2.6 on 2024-03-10 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_project_last_modify_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Цена проекта'),
        ),
    ]
