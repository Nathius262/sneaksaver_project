# Generated by Django 4.2.7 on 2024-01-11 05:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sneaksaver", "0009_alter_product_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="date",
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="booking",
            name="date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="contact",
            name="date",
            field=models.DateField(auto_now=True),
        ),
    ]
