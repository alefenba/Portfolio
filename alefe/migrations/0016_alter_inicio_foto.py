# Generated by Django 4.0.4 on 2022-04-28 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alefe', '0015_remove_sobre_perfil_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inicio',
            name='foto',
            field=models.ImageField(upload_to='s3://alefeportfolio/media/Perfil/'),
        ),
    ]
