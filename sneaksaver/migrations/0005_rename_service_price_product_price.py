# Generated by Django 4.2.7 on 2024-01-10 16:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("sneaksaver", "0004_product"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="service_price",
            new_name="price",
        ),
    ]
