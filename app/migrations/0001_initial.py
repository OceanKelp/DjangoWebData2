# Generated by Django 4.2.4 on 2023-12-15 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StockListNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stocklist_name', models.CharField(max_length=30)),
                ('SLdate_registered', models.DateField()),
                ('userowns', models.BooleanField()),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StockWatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_symbols', models.CharField(max_length=6)),
                ('stocklist_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stocklistnames')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StockOwn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_symbols', models.CharField(max_length=6)),
                ('stock_name', models.CharField(max_length=6)),
                ('stock_own', models.BooleanField()),
                ('stock_qty', models.DecimalField(decimal_places=5, max_digits=10)),
                ('stockdate_registered', models.DateTimeField()),
                ('stocklist_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stocklistnames')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
