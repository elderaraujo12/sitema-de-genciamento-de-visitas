# Generated by Django 4.1.3 on 2022-12-04 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgv_app', '0005_customuser_delete_morador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=14)),
                ('desc_visita', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=14)),
                ('desc_visita', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
