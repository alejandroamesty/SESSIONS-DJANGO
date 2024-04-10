import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sessions_component.db_component import check_user, update_login

@csrf_exempt
def login(request):
    if request.session.get('username'):
        return JsonResponse({"message": "Ya has iniciado sesión"})
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
        except json.JSONDecodeError:
            return JsonResponse({"error": "Los datos no son válidos"}, status=400)
        
        if not username or not password:
            return JsonResponse({"error": "Ingresa el usuario y la contraseña"}, status=400)
        
        user = check_user(username, password)
        if user:
            update_login(username)
            request.session['username'] = username
            return JsonResponse({"message": f"{username} ha iniciado sesión"})
        else:
            return JsonResponse({"error": "Usuario o contraseña inválida"}, status=401)
