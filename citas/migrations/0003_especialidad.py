# Generated by Django 4.1.3 on 2022-11-10 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0002_citas_especialidad_alter_citas_fecha_completada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Especialidad', models.CharField(max_length=100)),
            ],
        ),
    ]