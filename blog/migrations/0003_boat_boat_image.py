# Generated by Django 3.2.9 on 2021-11-10 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211110_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='boat',
            name='boat_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
