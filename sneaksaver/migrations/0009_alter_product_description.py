# Generated by Django 4.2.7 on 2024-01-10 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sneaksaver", "0008_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(),
        ),
    ]
