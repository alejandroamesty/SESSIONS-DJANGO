import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sessions_component.db_component import unregister_user

@csrf_exempt
def unregister(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
        except json.JSONDecodeError:
            return JsonResponse({"error": "Los datos no son válidos"}, status=400)

        if not username or not password:
            return JsonResponse({"error": "Ingresa el usuario y la contraseña"}, status=400)

        try:
            unregister_user(username, password)
            return JsonResponse({"message": "Usuario eliminado exitosamente"}, status=200)
        except Exception as e:
            print("Error al eliminar el usuario:", e)
            return JsonResponse({"error": "Error interno del servidor"}, status=500)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)