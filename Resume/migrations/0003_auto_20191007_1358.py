# Generated by Django 2.2.6 on 2019-10-07 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0002_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='Score',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
