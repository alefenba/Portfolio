# Generated by Django 4.0.4 on 2022-04-19 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alefe', '0013_rename_github_projeto_github_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificado',
            name='imagem_certificado',
            field=models.ImageField(upload_to='certificado/'),
        ),
        migrations.AlterField(
            model_name='inicio',
            name='foto',
            field=models.ImageField(upload_to='perfil/'),
        ),
        migrations.AlterField(
            model_name='sobre',
            name='perfil_img',
            field=models.ImageField(upload_to='perfil/'),
        ),
    ]
