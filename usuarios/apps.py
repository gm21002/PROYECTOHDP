from django.apps import AppConfig

# Definimos solo 1 aplicacion, en este caso "usuarios"
class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'
