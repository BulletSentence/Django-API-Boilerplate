# Generated by Django 4.1.7 on 2023-02-17 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(blank=True, choices=[('I', 'Intermediário'), ('A', 'Avançado'), ('B', 'Básico')], default='B', max_length=1),
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(choices=[('V', 'Vespertino'), ('N', 'Noturno'), ('M', 'Matiutino')], default='M', max_length=1)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.aluno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.curso')),
            ],
        ),
    ]
