# Generated by Django 4.1.3 on 2022-11-18 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('raquel', '0003_alter_comentarios_n_epoca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='impartidor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='impartidor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='manualidades',
            name='creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creador', to=settings.AUTH_USER_MODEL),
        ),
    ]