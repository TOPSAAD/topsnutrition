# Generated by Django 4.0.6 on 2023-01-20 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=20)),
                ('whatsapp', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=20)),
                ('ville', models.CharField(max_length=20)),
                ('pays', models.CharField(max_length=20)),
                ('products', models.CharField(max_length=10000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]