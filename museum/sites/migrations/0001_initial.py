# Generated by Django 3.2.7 on 2021-09-12 20:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('file_name', models.CharField(blank=True, max_length=50, null=True)),
                ('preview', models.CharField(blank=True, max_length=50)),
                ('file_type', models.CharField(blank=True, max_length=5)),
                ('original_scan', models.CharField(blank=True, max_length=5)),
                ('time_period', models.CharField(choices=[('FL', 'Flakkaserne and before'), ('G1', 'Grohn Barracks I'), ('DP', 'DP Camp Grohn'), ('G2', 'Grohn Barracks II'), ('RK', 'Roland-Kaserne'), ('JU', 'IUB-JU')], default='JU', max_length=2)),
                ('date_produced', models.DateField(default=datetime.date(1970, 1, 1))),
                ('author', models.CharField(max_length=40)),
                ('size', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=1500, null=True)),
                ('source', models.CharField(max_length=50)),
                ('signature', models.CharField(max_length=20)),
                ('copyright_status', models.CharField(max_length=10)),
                ('current_location', models.CharField(blank=True, max_length=20)),
                ('found_by', models.CharField(blank=True, max_length=30)),
                ('found_date', models.DateField(default=datetime.date(1970, 1, 1))),
                ('production_date', models.DateField(default=datetime.date(1970, 1, 1))),
                ('additional_info', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
