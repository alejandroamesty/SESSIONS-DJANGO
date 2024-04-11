from sessions_component.db_component import check_user_permissions, execute_method
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def process(request):
    # Verificar si el usuario ha iniciado sesión
    if not request.session.get('username'):
        return JsonResponse({"error": "Debes iniciar sesión para ejecutar métodos"}, status=401)

    try:
        data = json.loads(request.body)
        object_name = data.get('objectName')
        method_name = data.get('methodName')
        params = data.get('params', [])

        has_permission = check_user_permissions(request.session['username'], object_name, method_name)
        if not has_permission:
            return JsonResponse({"error": "No tienes permisos para ejecutar este método en este objeto"}, status=403)

        try:
            result = execute_method(object_name, method_name, *params)
            return JsonResponse({"result": result}, status=200)
        except ValueError as e:
            return JsonResponse({"error": f"Error interno del servidor al ejecutar el método: {e}"}, status=500)
    except Exception as e:
        return JsonResponse({"error": f"Error interno del servidor al verificar permisos: {e}"}, status=500)
