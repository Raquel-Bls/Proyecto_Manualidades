# Generated by Django 4.1.3 on 2022-11-18 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raquel', '0004_alter_curso_impartidor_alter_manualidades_creador'),
    ]

    operations = [
        migrations.AddField(
            model_name='epocas',
            name='impartidor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='imparti', to='raquel.curso'),
            preserve_default=False,
        ),
    ]