from rest_framework import permissions
from .models import CustomUser

class IsAdminUser(permissions.BasePermission):
    """
    Permissão personalizada para permitir acesso apenas a usuários com level 0 (administradores).
    """

    def has_permission(self, request, view):
        # Garante que o usuário está autenticado antes de prosseguir.
        if not request.user or not request.user.is_authenticated:
            return False
        
        # Verifica se o usuário autenticado tem um perfil CustomUser
        # e se o nível dele é 0.
        try:
            return request.user.custom_user.level == 0
        except CustomUser.DoesNotExist:
            # Se o CustomUser não existir por algum motivo, nega a permissão.
            return False
