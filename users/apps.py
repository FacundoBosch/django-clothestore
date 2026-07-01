from django.apps import AppConfig

# funcion personalizada para los users que chequea si pertenece o no a un grupo
def user_has_group(user, group):
    return user.groups.filter(name=group).exists()

def user_is_admin(user):
    return user.groups.filter(name='admins').exists()

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from django.contrib.auth.models import User
        User.add_to_class('has_group', user_has_group)
        User.add_to_class('is_admin', user_is_admin)
