# Generated by Django 3.2.7 on 2021-09-13 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_site_additional_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='date_produced',
            new_name='origin_date',
        ),
        migrations.AlterField(
            model_name='site',
            name='preview',
            field=models.FileField(upload_to=''),
        ),
    ]
