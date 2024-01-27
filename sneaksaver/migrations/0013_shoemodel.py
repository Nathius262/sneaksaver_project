# Generated by Django 4.2.7 on 2024-01-26 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneaksaver', '0012_alter_cleanservice_service_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
    ]