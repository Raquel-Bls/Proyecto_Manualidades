from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.


class Herramientas(models.Model):
    nom_herramienta = models.CharField(max_length=10)
    desc_herramienta = models.TextField(max_length=100)
    cantidad = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nom_herramienta


class Impartidor(models.Model):
    nom_imp = models.CharField(max_length=30)
    año_experiencia = models.PositiveIntegerField()
    idioma_imp = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.nom_imp


class Manualidades(models.Model):
    nombre = models.CharField(max_length=50)
    material = models.CharField(max_length=80)
    herramientas = models.ForeignKey(
        Herramientas, on_delete=models.CASCADE, related_name='herramientas',)  # -> modelo herramientas
    procedimiento = models.TextField(max_length=600)
    creador = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='creador',)
    video = models.URLField(null=True, blank=True,
                            verbose_name="Dirección Web")

    def __str__(self) -> str:
        return self.nombre

    def get_absolute_url(self):
        return reverse("manualidades_detalle", args=[str(self.id)])


class Curso(models.Model):
    nom_curso = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=500)
    impartidor = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='impartidor',)  # -> modelo impartidor
    horario = models.CharField(max_length=15)
    manualidades = models.ForeignKey(
        Manualidades, on_delete=models.CASCADE, related_name='manualidades',)  # -> modelo manualidades

    def __str__(self) -> str:
        return self.nom_curso

    def get_absolute_url(self):
        return reverse("cursos_detalle", args=[str(self.id)])


class Dificultad(models.Model):
    difi_nom = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.difi_nom


class Epocas(models.Model):
    Epoca_nom = models.CharField(max_length=14)
    epoca_desc = models.TextField(max_length=100)
    fecha_epoca = models.DateTimeField(auto_now_add=True)
    curso = models.ForeignKey(
        Curso, on_delete=models.CASCADE, related_name='curso',)  # -> modelo curso
    dificultad = models.ForeignKey(
        Dificultad, on_delete=models.CASCADE, related_name='dificultad')  # -> modelo dificultad
    impartidor = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='imparti',)

    def __str__(self) -> str:
        return self.Epoca_nom

    def get_absolute_url(self):
        return reverse("epocas_detalle", args=[str(self.id)])


class Comentarios(models.Model):
    nom_curso = models.ForeignKey(
        Curso, on_delete=models.CASCADE, related_name='comentario',)
    Comentario = models.CharField(max_length=200)
    NombreU = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self) -> str:
        return self.Comentario

    def get_absolute_url(self):
        return reverse("cursos_detalle", args=[str(self.nom_curso_id)])


class ComentariosM(models.Model):
    nom_manualidad = models.ForeignKey(
        Manualidades, on_delete=models.CASCADE, related_name='comentarioM',)
    ComentarioM = models.CharField(max_length=200)
    NombreUM = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self) -> str:
        return self.ComentarioM

    def get_absolute_url(self):
        return reverse("manualidades_detalle", args=[str(self.nom_manualidad_id)])


# class ComentariosE(models.Model):
 #   nom_epocas = models.ForeignKey(
  #      Epocas, on_delete=models.CASCADE, related_name='comentarioE',)
   # ComentarioE = models.CharField(max_length=200)
    #NombreUE = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    # def __str__(self) -> str:
     #   return self.ComentarioE

    # def get_absolute_url(self):
     #   return reverse("epocas_detalle", args=[str(self.nom_epocas_id)])

 # N_Manualidad = models.ForeignKey(
    #   Manualidades, on_delete=models.CASCADE, related_name='comentMan',)
    # N_Epoca = models.ForeignKey(
    #  Epocas, on_delete=models.CASCADE, related_name='comentEpoca',)

   # def get_absolute_url(self):
    #    return reverse("manualidades_detalle", args=[str(self.manualidades_id)])

    # def get_absolute_url(self):
     #   return reverse("epocas_detalle", args=[str(self.epocas_id)])
