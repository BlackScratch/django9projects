# Generated by Django 5.0.2 on 2024-02-15 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_dt', models.DateTimeField(auto_now=True)),
                ('order_name', models.CharField(max_length=200)),
                ('order_phone', models.CharField(max_length=200)),
            ],
        ),
    ]
