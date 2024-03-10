# Generated by Django 4.2.6 on 2024-03-10 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Работника', 'verbose_name_plural': 'Работники'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Работник'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='reservation_percent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Загруженность работника'),
        ),
    ]
