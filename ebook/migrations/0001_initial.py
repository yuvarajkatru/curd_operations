# Generated by Django 3.2 on 2022-01-21 07:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField(max_length=250)),
                ('Author', models.TextField(max_length=250)),
                ('Genre', models.CharField(choices=[('Fantasy', 'Fantasy'), ('Literary', 'Literary'), ('Mystery', 'Mystery'), ('Non-Fiction', 'Non-Fiction'), ('Science Fiction', 'Science Fiction'), ('Thriller', 'Thriller')], max_length=100, null=True)),
                ('Review', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Favorite', models.BooleanField()),
            ],
        ),
    ]
