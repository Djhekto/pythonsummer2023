# Generated by Django 4.2.4 on 2023-08-07 08:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_product_smthnew"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="ahah",
            field=models.TextField(blank=True),
        ),
    ]
