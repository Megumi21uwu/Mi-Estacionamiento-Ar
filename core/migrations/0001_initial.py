# Generated by Django 4.0.4 on 2022-11-23 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Estacionamiento',
            fields=[
                ('idTipoEsta', models.AutoField(primary_key=True, serialize=False)),
                ('tipoEsta', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Usuario',
            fields=[
                ('idTipo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('run', models.IntegerField()),
                ('dv', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=60)),
                ('apellidopaterno', models.CharField(max_length=60)),
                ('apellidomaterno', models.CharField(max_length=60)),
                ('correo', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=12)),
                ('username', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('idTipo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.tipo_usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('idEstacionamiento', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=100)),
                ('cantidadVehiculo', models.IntegerField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('idTipoEsta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipo_estacionamiento')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
    ]
