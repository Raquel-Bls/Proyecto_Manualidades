# from django.shortcuts import render
# Obliga a que estes logueado para poder visualizar la vista#
from django.contrib.auth.mixins import LoginRequiredMixin
# Valida los permisos
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# , Herramientas, Impartidor, Dificultad
from .models import Comentarios, Curso, Manualidades, Epocas,  ComentariosM
# Para que te regrese a la pagina principal de una manera mas lentaComentariosE,
from django.urls import reverse_lazy
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required

# -------------------- CURSOS ---------------------------


class cursosPageview(LoginRequiredMixin, ListView):
    template_name = 'cursos.html'
    model = Curso
    context_object_name = 'Todos_Cursos'
    login_url = 'login'


class cursosPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'cursos_detalle.html'
    model = Curso
    context_object_name = 'Todos_Cursos'
    login_url = 'login'


class cursosPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'cursos_nuevo.html'
    model = Curso
    fields = ('nom_curso', 'descripcion',
              'impartidor', 'horario', 'manualidades')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.impartidor = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseNotFound('<h1> NO SE CUENTA CON ACCESO PARA REALIZAR ESE CAMBIO </h1>')


class cursosPageUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'cursos_editar.html'
    model = Curso
    fields = ['descripcion', 'horario', 'manualidades']
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.impartidor != self.request.user:
            return HttpResponseNotFound('<h1><br> NO SE CUENTA CON ACCESO PARA REALIZAR ESE CAMBIO </h1>')
        return super().dispatch(request, *args, **kwargs)


class cursosPageDelete(LoginRequiredMixin, DeleteView):
    template_name = 'cursos_eliminar.html'
    model = Curso
    fields = "_all_"
    success_url = reverse_lazy('cursos')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.impartidor != self.request.user:
            return HttpResponseNotFound('<h1><br> NO SE CUENTA CON ACCESO PARA REALIZAR ESE CAMBIO </h1>')
            # return HttpResponseNotFound('<div class="alert alert-secondary" role="alert"> NO SE CUENTA CON ACCESO PARA REALIZAR ESE CAMBIO </div>')
        return super().dispatch(request, *args, **kwargs)

# -------------------- MANUALIDADES ---------------------------


class manualidadesPageview(LoginRequiredMixin, ListView):
    template_name = 'manualidades.html'
    model = Manualidades
    context_object_name = 'Todos_Manualidades'
    login_url = 'login'


class manualidadesPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'manualidades_detalle.html'
    model = Manualidades
    context_object_name = 'Todos_Manualidades'
    login_url = 'login'


class manualidadesPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'manualidades_nuevo.html'
    model = Manualidades
    fields = ('nombre', 'material',
              'herramientas', 'procedimiento', 'creador', 'video')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseNotFound('<h1> NO SE CUENTA CON ACCESO PARA REALIZAR ESE CAMBIO </h1>')


class manualidadesPageUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'manualidades_editar.html'
    model = Manualidades
    fields = ['herramientas', 'procedimiento', 'video']
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.creador != self.request.user:
            return HttpResponseNotFound('<h1><br> NO SE CUENTA CON ACCESO PARA REALIZAR ESE CAMBIO </h1>')
        return super().dispatch(request, *args, **kwargs)


class manualidadesPageDelete(LoginRequiredMixin, DeleteView):
    template_name = 'manualidades_eliminar.html'
    model = Manualidades
    fields = "_all_"
    success_url = reverse_lazy('manualidades')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.creador != self.request.user:
            return HttpResponseNotFound('<h1><br> NO SE CUENTA CON ACCESO PARA REALIZAR ESE CAMBIO </h1>')
        return super().dispatch(request, *args, **kwargs)


# -------------------- EPOCAS ---------------------------
class epocasPageview(LoginRequiredMixin, ListView):
    template_name = 'epocas.html'
    model = Epocas
    context_object_name = 'Todos_Epocas'
    login_url = 'login'


class epocasPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'epocas_detalle.html'
    model = Epocas
    context_object_name = 'Todos_Epocas'
    login_url = 'login'


class epocasPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'epocas_nuevo.html'
    model = Epocas
    fields = ('Epoca_nom', 'epoca_desc',
              'curso', 'dificultad', 'impartidor')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
            # return login_required(super(LoginRequiredMixin).as_view())
        return HttpResponseNotFound('<h1> NO SE CUENTA CON ACCESO PARA REALIZAR ESE CAMBIO </h1>')

     # def dispatch(self, request, *args, **kwargs):
      #  if not request.user.has_perms(self.required_permissions):
       #     messages.error(request,'You do not have the permission required to perform the ''requested operation.')
        #    return redirect(settings.LOGIN_URL)}
        # return login_required(super(LoginRequiredMixin, cls).as_view())
        # return super(PermissionsRequiredMixin, self).dispatch(
        #   request, *args, **kwargs)


class epocasPageUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'epocas_editar.html'
    model = Epocas
    fields = ['epoca_desc', 'curso', 'dificultad']
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseNotFound('<h1> NO SE CUENTA CON ACCESO PARA REALIZAR ESE CAMBIO </h1>')


class epocasPageDelete(LoginRequiredMixin, DeleteView):
    template_name = 'epocas_eliminar.html'
    model = Epocas
    fields = "_all_"
    success_url = reverse_lazy('epocas')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.impartidor != self.request.user:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied


# ------------------ COMENTARIOS ------------------------
class comentriosPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'comentarios.html'
    model = Comentarios
    fields = ('Comentario',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.NombreU = self.request.user
        form.instance.nom_curso_id = self.kwargs['pk']
        return super().form_valid(form)


class comentriosMPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'comentariosM.html'
    model = ComentariosM
    fields = ('ComentarioM',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.NombreUM = self.request.user
        form.instance.nom_manualidad_id = self.kwargs['pk']
        return super().form_valid(form)


# class comentriosPageCreate(LoginRequiredMixin, CreateView):
 #   template_name = 'comentarios.html'
  #  model = ComentariosE
   # fields = ('Comentario',)
    #login_url = 'login'

    # def form_valid(self, form):
     #   form.instance.NombreU = self.request.user
      #  form.instance.nom_epocas_id = self.kwargs['pk']
       # return super().form_valid(form)


class comentriosPageDelete(LoginRequiredMixin, DeleteView):
    template_name = 'comentarios_eliminar.html'
    model = Comentarios
    fields = "_all_"
    success_url = reverse_lazy('cursos')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseNotFound('<h1> NO SE CUENTA CON ACCESO PARA REALIZAR ESE CAMBIO </h1>')


class comentriosMPageDelete(LoginRequiredMixin, DeleteView):
    template_name = 'comentariosM_eliminar.html'
    model = ComentariosM
    fields = "_all_"
    success_url = reverse_lazy('manualidades')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseNotFound('<h1> NO SE CUENTA CON ACCESO PARA REALIZAR ESE CAMBIO </h1>')

# Create your views here.
