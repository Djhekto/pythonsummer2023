# Generated by Django 4.2.4 on 2023-08-07 08:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="smthnew",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
