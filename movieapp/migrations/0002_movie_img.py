# Generated by Django 4.2.2 on 2023-06-10 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='img', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
