# Generated by Django 4.1.3 on 2023-01-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_blog', '0004_mensaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebSiteSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('sub_titulo', models.CharField(max_length=100)),
            ],
        ),
    ]