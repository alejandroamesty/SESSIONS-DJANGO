import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sessions_component.db_component import change_password

@csrf_exempt
def changepassword(request):
    if not request.session.get('username'):
        return JsonResponse({"error": "Debes iniciar sesión para cambiar la contraseña"}, status=401)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = request.session.get('username')
            old_password = data.get('oldPassword')
            new_password = data.get('newPassword')
        except json.JSONDecodeError:
            return JsonResponse({"error": "Los datos no son válidos"}, status=400)

        if not old_password or not new_password:
            return JsonResponse({"error": "Ingresa la contraseña antigua y la nueva contraseña"}, status=400)

        try:
            change_password(username, old_password, new_password)
            return JsonResponse({"message": "Contraseña actualizada exitosamente"})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=401)