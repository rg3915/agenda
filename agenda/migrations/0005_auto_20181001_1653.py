# Generated by Django 2.1.1 on 2018-10-01 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_auto_20180928_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='cargo',
            field=models.CharField(default='estagio', max_length=100, verbose_name='Cargo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='celular',
            field=models.CharField(max_length=9, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='sexo',
            field=models.CharField(choices=[('HOMEM', 'Homem'), ('MULHER', 'Mulher')], max_length=6),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='telefone',
            field=models.CharField(max_length=9, verbose_name='Tel.Fixo'),
        ),
    ]
