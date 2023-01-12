# Generated by Django 4.1.5 on 2023-01-07 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Angajati',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=100)),
                ('varsta', models.PositiveIntegerField(max_length=90)),
                ('status', models.BooleanField(default=1)),
            ],
        ),
    ]