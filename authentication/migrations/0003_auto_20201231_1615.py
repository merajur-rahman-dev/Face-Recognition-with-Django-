# Generated by Django 3.1.4 on 2020-12-31 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_useralert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useralert',
            name='alert_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
