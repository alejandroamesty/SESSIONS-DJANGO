import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sessions_component.db_component import check_user_permissions

@csrf_exempt
def checkpermissions(request):
    if not request.session.get('username'):
        return JsonResponse({"error": "Debes iniciar sesión para verificar permisos"}, status=401)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            method_name = data.get('methodName')
            object_name = data.get('objectName')
        except json.JSONDecodeError:
            return JsonResponse({"error": "Los datos no son válidos"}, status=400)

        if not method_name or not object_name:
            return JsonResponse({"error": "Faltan datos"}, status=400)

        has_permission = check_user_permissions(request.session['username'], object_name, method_name)

        if has_permission:
            return JsonResponse({"message": "Tienes permisos para ejecutar este método en este objeto"})
        else:
            return JsonResponse({"error": "No tienes permisos para ejecutar este método en este objeto"}, status=403)