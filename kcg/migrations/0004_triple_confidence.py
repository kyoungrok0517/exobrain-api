# Generated by Django 2.0.7 on 2018-07-31 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kcg', '0003_auto_20180730_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='triple',
            name='confidence',
            field=models.FloatField(null=True),
        ),
    ]
