# Generated by Django 4.2.7 on 2024-01-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneaksaver', '0011_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleanservice',
            name='service_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, null=True),
        ),
    ]