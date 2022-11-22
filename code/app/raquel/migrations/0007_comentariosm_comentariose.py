# Generated by Django 4.1.3 on 2022-11-20 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('raquel', '0006_remove_comentarios_n_curso_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentariosM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comentario', models.CharField(max_length=200)),
                ('NombreU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('nom_manualidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to='raquel.manualidades')),
            ],
        ),
        migrations.CreateModel(
            name='ComentariosE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comentario', models.CharField(max_length=200)),
                ('NombreU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('nom_epocas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to='raquel.epocas')),
            ],
        ),
    ]