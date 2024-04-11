import importlib
import sys
import os
from django.db import connection
from .sql_queries import CHECK_USER, UPDATE_LOGIN, CHANGE_PASSWORD, CREATE_USER, ASSIGN_ROLE, DELETE_ROLE, CHECK_ROLE, CHECK_PERMISSION, DELETE_USER

def check_user(username, password):
    with connection.cursor() as cursor:
        cursor.execute(CHECK_USER, [username, password])
        return cursor.fetchone()

def update_login(username):
    with connection.cursor() as cursor:
        cursor.execute(UPDATE_LOGIN, [username])

def change_password(username, old_password, new_password):
    with connection.cursor() as cursor:
        cursor.execute(CHECK_USER, [username, old_password])
        user = cursor.fetchone()
        if not user:
            raise ValueError("Usuario o contraseña antigua inválida")

        cursor.execute(CHANGE_PASSWORD, [new_password, username])

        return True

def create_user(username, password, email):
    with connection.cursor() as cursor:
        cursor.execute(CREATE_USER, [username, password, email])
        user_id = cursor.fetchone()[0]
        cursor.execute(ASSIGN_ROLE, [user_id, 3])

def unregister_user(username, password):
    with connection.cursor() as cursor:
        cursor.execute(CHECK_USER, [username, password])
        user = cursor.fetchone()
        if not user:
            raise ValueError("Usuario o contraseña inválida")
        
        user_id = user[0]
        cursor.execute(DELETE_ROLE, [user_id])
        cursor.execute(DELETE_USER, [username])

        return True

def check_user_permissions(username, object_name, method_name):
    with connection.cursor() as cursor:

        cursor.execute(CHECK_ROLE, [username])
        roles = cursor.fetchall()
        role_ids = [role[0] for role in roles]

        for role_id in role_ids:
            cursor.execute(CHECK_PERMISSION, [role_id, method_name, object_name])
            permission = cursor.fetchone()
            if permission:
                return True

        return False

def execute_method(object_name, method_name, *params):
    try:
        print(f"Ejecutando método {method_name} en el objeto {object_name}")

        bo_directory = os.path.join(os.path.dirname(__file__), 'BO')
        sys.path.append(bo_directory)

        obj_module = importlib.import_module(object_name)

        obj_class = getattr(obj_module, object_name)

        instance = obj_class()

        result = getattr(instance, method_name)(*params)
        print(f"Resultado de {method_name}: {result}")

        sys.path.remove(bo_directory)

        return result
    except Exception as e:
        print(f"Error al ejecutar el método: {e}")
        raise ValueError(f"Error al ejecutar el método: {e}")