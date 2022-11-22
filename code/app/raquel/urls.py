from django.urls import path
from .views import cursosPageview, cursosPageCreate, cursosPageDetail, cursosPageUpdate, cursosPageDelete, comentriosPageCreate, comentriosPageDelete, manualidadesPageCreate,  manualidadesPageview
from .views import manualidadesPageDetail, manualidadesPageUpdate, manualidadesPageDelete, comentriosMPageCreate, comentriosMPageDelete, epocasPageview, epocasPageCreate, epocasPageDetail, epocasPageUpdate, epocasPageDelete


urlpatterns = [
    # --------------------- CURSOS -------------
    path('cursos/', cursosPageview.as_view(), name='cursos'),
    path('cursos/<int:pk>', cursosPageDetail.as_view(), name='cursos_detalle'),
    path('cursos/nuevo', cursosPageCreate.as_view(), name='cursos_nuevo'),
    path('cursos/<int:pk>/editar/',
         cursosPageUpdate.as_view(), name='cursos_editar'),
    path('cursos/<int:pk>/eliminar/',
         cursosPageDelete.as_view(), name='cursos_eliminar'),
    # --------------------- MANUALIDADES -------------
    path('manualidades/', manualidadesPageview.as_view(), name='manualidades'),
    path('manualidades/<int:pk>', manualidadesPageDetail.as_view(),
         name='manualidades_detalle'),
    path('manualidades/nuevo', manualidadesPageCreate.as_view(),
         name='manualidades_nuevo'),
    path('manualidades/<int:pk>/editar/',
         manualidadesPageUpdate.as_view(), name='manualidades_editar'),
    path('manualidades/<int:pk>/eliminar/',
         manualidadesPageDelete.as_view(), name='manualidades_eliminar'),
    # --------------------- EPOCAS -------------
    path('epocas/', epocasPageview.as_view(), name='epocas'),
    path('epocas/<int:pk>', epocasPageDetail.as_view(),
         name='epocas_detalle'),
    path('epocas/nuevo', epocasPageCreate.as_view(),
         name='epocas_nuevo'),
    path('epocas/<int:pk>/editar/',
         epocasPageUpdate.as_view(), name='epocas_editar'),
    path('epocas/<int:pk>/eliminar/',
         epocasPageDelete.as_view(), name='epocas_eliminar'),
    # --------------------COMENTARIOS------------
    path('<int:pk>/comentarios/',
         comentriosPageCreate.as_view(), name='comentarios'),
    path('<int:pk>/comentariosM/',
         comentriosMPageCreate.as_view(), name='comentariosM'),
    path('comentarios/<int:pk>/eliminar/',
         comentriosPageDelete.as_view(), name='comentarios_eliminar'),
    path('comentariosM/<int:pk>/eliminar/',
         comentriosMPageDelete.as_view(), name='comentariosM_eliminar'),
]
