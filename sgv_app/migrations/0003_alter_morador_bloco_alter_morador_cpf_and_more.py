# Generated by Django 4.1.3 on 2022-12-04 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgv_app', '0002_alter_morador_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='morador',
            name='bloco',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='morador',
            name='cpf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='morador',
            name='num_apartamento',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='morador',
            name='senha',
            field=models.IntegerField(),
        ),
    ]
