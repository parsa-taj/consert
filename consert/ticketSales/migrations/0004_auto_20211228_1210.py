# Generated by Django 3.2.9 on 2021-12-28 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticketSales', '0003_remove_timeconsert_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timeconsert',
            options={'ordering': ('-start_time',), 'verbose_name': 'Time', 'verbose_name_plural': 'Times'},
        ),
        migrations.AlterField(
            model_name='timeconsert',
            name='consert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeConsert', to='ticketSales.consert', verbose_name='time consert'),
        ),
        migrations.AlterField(
            model_name='timeconsert',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeLocation', to='ticketSales.location', verbose_name='time location'),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketSales.consert', verbose_name='consert')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Favorites', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Favorite',
                'verbose_name_plural': 'Favorites',
            },
        ),
    ]
