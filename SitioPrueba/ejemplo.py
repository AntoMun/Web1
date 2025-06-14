# Diccionario para almacenar usuarios y contraseñas
usuarios = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2"
}

def inicio_sesion():
    print("Bienvenido al sistema de inicio de sesión")

    # Solicitar al usuario que ingrese su nombre de usuario y contraseña
    username = input("Por favor, ingresa tu nombre de usuario: ")
    password = input("Por favor, ingresa tu contraseña: ")

    # Verificar si el usuario existe y si la contraseña es correcta
    if username in usuarios and usuarios[username] == password:
        print("¡Inicio de sesión exitoso!")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

# Llamar a la función de inicio de sesión terminar
inicio_sesion()