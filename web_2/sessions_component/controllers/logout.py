from django.http import JsonResponse

def logout(request):
    if 'username' not in request.session:
        return JsonResponse({"error": "No has iniciado sesión"}, status=401)
    
    del request.session['username']
    return JsonResponse({"message": "Se cerró la sesión exitosamente"})
