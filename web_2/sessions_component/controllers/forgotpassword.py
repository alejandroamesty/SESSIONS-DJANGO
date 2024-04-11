import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sessions_component.db_component import get_username_by_email, add_temporary_password
from django.core.mail import send_mail
from django.http import JsonResponse


@csrf_exempt
def forgotpassword(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            if not email:
                return JsonResponse({"error": "Ingresa tu dirección de correo electrónico"}, status=400)

            
            username = get_username_by_email(email)
            if not username:
                return JsonResponse({"error": "No se encontró ningún usuario asociado a esta dirección de correo electrónico"}, status=404)

          
            temporary_password = generate_temporary_password(10)
            add_temporary_password(username, temporary_password, temporary=True, expiration_date=calculate_expiration_date())

          

            return JsonResponse({"message": "Se ha generado una nueva contraseña temporal. Revisa tu correo electrónico."})
        except Exception as e:
           
            print(f"Error al restablecer la contraseña: {e}")
            return JsonResponse({"error": "Error interno del servidor al restablecer la contraseña"}, status=500)

    return JsonResponse({"error": "Método no permitido"}, status=405)

def generate_temporary_password(length):
    import random
    import string
    
    
    chars = string.ascii_letters + string.digits
    temporary_password = ''.join(random.choice(chars) for _ in range(length))
    
    return temporary_password

def calculate_expiration_date():
    import datetime
    
   
    expiration_date = datetime.datetime.now() + datetime.timedelta(hours=1)
    
    return expiration_date



def send_temporary_password_email(email, temporary_password):
    subject = "Contraseña temporal"
    message = f"Tu contraseña temporal es: {temporary_password}. Por favor, cámbiala después de iniciar sesión."
    from_email = "tatoxpro01@gmail.com"  
    recipient_list = [email]

    try:
        # Enviar el correo electrónico
        send_mail(subject, message, from_email, recipient_list)
        return True  
    except Exception as e:
        # Manejar cualquier error al enviar el correo electrónico
        print(f"Error al enviar el correo electrónico: {e}")
        return False  

@csrf_exempt
def forgotpassword(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            if not email:
                return JsonResponse({"error": "Ingresa tu dirección de correo electrónico"}, status=400)

           
            username = get_username_by_email(email)
            if not username:
                return JsonResponse({"error": "No se encontró ningún usuario asociado a esta dirección de correo electrónico"}, status=404)

            temporary_password = generate_temporary_password(10)
            add_temporary_password(username, temporary_password, temporary=True, expiration_date=calculate_expiration_date())

          
            enviado_correctamente = send_temporary_password_email(email, temporary_password)
            if enviado_correctamente:
                return JsonResponse({"message": "Se ha generado una nueva contraseña temporal. Revisa tu correo electrónico."})
            else:
                return JsonResponse({"error": "Error al enviar el correo electrónico con la contraseña temporal."}, status=500)
        
        except Exception as e:
           
            print(f"Error al restablecer la contraseña: {e}")
            return JsonResponse({"error": "Error interno del servidor al restablecer la contraseña"}, status=500)

    return JsonResponse({"error": "Método no permitido"}, status=405)