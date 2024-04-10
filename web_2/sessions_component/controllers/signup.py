import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sessions_component.db_component import check_user, create_user

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')
        except json.JSONDecodeError:
            return JsonResponse({"error": "Los datos no son válidos"}, status=400)

        if not username or not password or not email:
            return JsonResponse({"error": "Ingresa el usuario, la contraseña y el email"}, status=400)

        user = check_user(username, password)
        if user:
            return JsonResponse({"error": "El usuario ya existe"}, status=409)
        else:
            try:
                create_user(username, password, email)
                return JsonResponse({"message": "Usuario creado exitosamente"}, status=201)
            except Exception as e:
                print("Error al crear el usuario:", e)
                return JsonResponse({"error": "Error interno del servidor"}, status=500)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)