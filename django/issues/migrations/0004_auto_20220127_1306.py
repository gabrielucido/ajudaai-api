# Generated by Django 3.1.14 on 2022-01-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_issuesearchfields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['-created_at'], 'verbose_name': 'Problema', 'verbose_name_plural': 'Problemas'},
        ),
        migrations.AlterField(
            model_name='issue',
            name='image',
            field=models.TextField(blank=True, null=True, verbose_name='Imagem'),
        ),
    ]
