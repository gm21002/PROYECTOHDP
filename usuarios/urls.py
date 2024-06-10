from django.urls import path
from . import views

urlpatterns = [
    # Para Iniciar Sesion
    path('', views.login, name='login'),
        
    # Path para inicio
    path('inicio', views.inicio, name='inicio'),

    #Path para graficos
    path('data/', views.chart_data, name='chart_data'),

     path('data/razon_encuesta/', views.chart_data_razon_encuesta, name='chart_data_razon_encuesta'),  # Nueva ruta para los datos de razon_encuesta
    # Otros paths aquí
     path('data/ventajas_encuesta/', views.chart_data_ventajas_encuesta, name='chart_data_ventajas_encuesta'),

     path('data/desventajas_encuesta/', views.chart_data_desventajas_encuesta, name='chart_data_desventajas_encuesta'),
     path('data/poraum_encuesta/', views.chart_data_poraum_encuesta, name='chart_data_poraum_encuesta'),

    # Path para Usuario
     path('registrar-nuevo-usuario_inicio/', views.registrar_usuario_inicio,
         name='registrar_usuario_inicio'),
    path('registrar-nuevo-usuario/', views.registrar_usuario,
         name='registrar_usuario'),
    path('lista-de-usuarios/', views.listar_usuarios, name='listar_usuarios'),

    path('detalles-del-usuario/<str:id>/',
         views.detalles_usuario, name='detalles_usuario'),

    path('formulario-para-actualizar-usuario/<str:id>/',
         views.view_form_update_usuario, name='view_form_update_usuario'),

    path('actualizar-usuario/<str:id>/',
         views.actualizar_usuario, name='actualizar_usuario'),
    path('eliminar-usuario/', views.eliminar_usuario, name='eliminar_usuario'),

    # Path para Encuesta
    path('agregar-nuevo-encuesta/', views.agregar_encuesta,
         name='agregar_encuesta'),
    path('lista-de-encuestas/', views.listar_encuestas, name='listar_encuestas'),

    path('detalles-del-encuesta/<str:id>/',
         views.detalles_encuesta, name='detalles_encuesta'),

    path('formulario-para-actualizar-encuesta/<str:id>/',
         views.view_form_update_encuesta, name='view_form_update_encuesta'),

    path('actualizar-encuesta/<str:id>/',
         views.actualizar_encuesta, name='actualizar_encuesta'),
    path('eliminar-encuesta/', views.eliminar_encuesta, name='eliminar_encuesta'),

]
