# Generated by Django 4.0.6 on 2022-09-04 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-price']},
        ),
    ]
