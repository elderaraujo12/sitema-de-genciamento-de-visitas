# Generated by Django 4.1.3 on 2022-12-04 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgv_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='morador',
            name='telefone',
            field=models.IntegerField(),
        ),
    ]
