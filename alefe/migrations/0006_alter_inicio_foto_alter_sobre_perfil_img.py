# Generated by Django 4.0.2 on 2022-03-29 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alefe', '0005_alter_projeto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inicio',
            name='foto',
            field=models.ImageField(upload_to='Perfil/'),
        ),
        migrations.AlterField(
            model_name='sobre',
            name='perfil_img',
            field=models.ImageField(upload_to='Perfil/'),
        ),
    ]
