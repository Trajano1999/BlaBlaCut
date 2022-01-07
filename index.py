# -------------------------------------------------------------------------------------------------
#  
#   PRÁCTICA 3
#   DDSI GRUPO SIMPLE      
#       Marta Gómez Sánchez
#       Juan Manuel Mateos Pérez
#       Mario Sánchez-Migallón López
#       Marta Soto Werner
#   
#   Escuela Superior de Ingeniería Informática y Telecomunicaciones
#   Curso académico 2021/2022
#
# -------------------------------------------------------------------------------------------------

import cx_Oracle
import os                                                                                          # para limpiar la consola

# -------------------------------------------------------------------------------------------------
# DECLARACIÓN DE LOS MENÚS
# -------------------------------------------------------------------------------------------------

def MenuLogin():
    print(" ______  _         ______  _          _____         _    ")
    print(" | ___ \| |        | ___ \| |        /  __ \       | |   ")
    print(" | /_/ /| |  __ _  | |_/ /| |  __ _ |  /  \/ _   _ | |_  ")
    print(" | ___ \| | / _` | | ___ \| | / _` || |     | | | || __| ")
    print(" | |_/ /| || (_| | | |_/ /| || (_| ||  \__/|| |_| || |_  ")
    print(" \____/ |_| \__,_| \____/ |_| \__,_| \____/ \__,__| \__| ")    
    print()
    print("1.- Iniciar sesión")
    print("2.- Crear cuenta como Cliente")
    print("3.- Crear cuenta como Peluquero")
    print("4.- Salir")
    print()

def MenuPrincipal():
    print(" ___  ___                  ______     _            _             _  ")
    print(" |  \/  |                  | ___ \   (_)          (_)           | | ")
    print(" | .  . | ___ _ __  _   _  | |_/ / __ _ _ __   ___ _ _ __   __ _| | ")
    print(" | |\/| |/ _ \ '_ \| | | | |  __/ '__| | '_ \ / __| | '_ \ / _` | | ")
    print(" | |  | |  __/ | | | |_| | | |  | |  | | | | | (__| | |_) | (_| | | ")
    print(" \_|  |_/\___|_| |_|\__,_| \_|  |_|  |_|_| |_|\___|_| .__/ \__,_|_| ")
    print("                                                    | |             ")
    print("                                                    |_|             ")
    print("1.- Perfil")
    print("2.- Ver listado de Peluqueros")
    print("3.- Citas")                                                                             # consumir producto en cita
    print("4.- Mensajes")
    print("5.- Valoraciones")
    print("6.- Incidencias")
    print("7.- Almacén")
    print("8.- Cerrar Sesión")
    print()

def MenuPerfil():
    print()
    print("1.- Ver Perfil")
    print("2.- Modificar Perfil")
    print("3.- Eliminar Perfil")                                                                   # solo si es peluquero
    print("4.- Volver atrás")
    print()

def MenuCitas():
    print()
    print("1.- Ver citas")
    print("2.- Crear una cita")                                                                    # realizar el pago tras crear una cita
    print("3.- Eliminar una cita")
    print("4.- Modificar una cita")
    print("5.- Volver atrás")
    print()

def MenuMensajes():
    print()
    print("1.- Escribir un mensaje")
    print("2.- Eliminar un mensaje")
    print("3.- Volver atrás")
    print()

def MenuValoraciones():
    print()
    print("1.- Añadir valoración")
    print("2.- Añadir comentario")
    print("3.- Añadir fotorafía")
    print("4.- Volver atrás")
    print()

def MenuAlmacen():
    print()
    print("1.- Crear almacén")
    print("2.- Encargar productos")
    print("3.- Eliminar almacén")
    print("4.- Volver atrás")
    print()

# -------------------------------------------------------------------------------------------------
# LETREROS
# -------------------------------------------------------------------------------------------------

def LetreroAccesoCuenta():
    print("\t--------------------------")
    print("\t|   ACCESO A LA CUENTA   |")
    print("\t--------------------------")
    print()

def LetreroCreacionCuentaCliente():
    print("\t----------------------------------")
    print("\t|   CREACIÓN DE CUENTA CLIENTE   |")
    print("\t----------------------------------")
    print()

def LetreroCreacionCuentaPeluquero():
    print("\t------------------------------------")
    print("\t|   CREACIÓN DE CUENTA PELUQUERO   |")
    print("\t------------------------------------")
    print()

# -------------------------------------------------------------------------------------------------
# CREACION DE LAS CUENTAS
# -------------------------------------------------------------------------------------------------

def CreacionCuentaUsuario(valor):
    print("DNI:"); dni = input()
    cursor.execute("SELECT count(*) FROM usuarios WHERE dni = '" + dni + "'")
    res_dni = cursor.fetchall()
    while res_dni[0][0] != 0:
        os.system('clear')
        print("Ya existe un usuario con ese DNI"); 
        print()

        LetreroCreacionCuentaCliente()
        print("DNI:"); dni = input()
        cursor.execute("SELECT count(*) FROM usuarios WHERE dni = '" + dni + "'")
        res_dni = cursor.fetchall()

    print("Nombre usuario:");       nombre_usuario = input()
    print("Contraseña:");                 password = input()
    print("Nombre y Apellidos:"); nombre_apellidos = input()
    print("Fecha Nacimiento:");              fecha = input()
    print("Correo electrónico:");           correo = input()

    cursor.execute("INSERT INTO usuarios VALUES ('" + dni + "', '" + nombre_usuario + "', '" + password + "', '" + nombre_apellidos + "', TO_DATE('" + fecha + "', 'DD/MM/YYYY'), '" + correo + "', '" + str(valor) + "')")
    
    # agregamos dni a tabla clientes
    if str(valor) == "0":
        cursor.execute("INSERT INTO clientes VALUES ('" + dni + "')")
    else:
        print("CNAE:");                 cnae = input()
        print("Localización:"); localizacion = input()
        cursor.execute("INSERT INTO peluqueros VALUES ('" + dni + "', '" + cnae + "', '" + localizacion + "')")

    # jjj no se si es necesario el commit
    cursor.execute("COMMIT")

def CreacionCuentaCliente():
    LetreroCreacionCuentaCliente()
    CreacionCuentaUsuario(0)
    os.system('clear')

def CreacionCuentaPeluquero():
    LetreroCreacionCuentaPeluquero()
    CreacionCuentaUsuario(1)
    os.system('clear')

# -------------------------------------------------------------------------------------------------
# FUNCIONES ADICIONALES
# -------------------------------------------------------------------------------------------------

def ComprobacionLogin():
    LetreroAccesoCuenta()
    print("DNI:"); dni = input()
    cursor.execute("SELECT count(*) FROM usuarios WHERE dni = '" + dni + "'")
    res_dni = cursor.fetchall()

    while res_dni[0][0] == 0:
        os.system('clear')
        print("No existe este usuario"); 
        print()

        LetreroAccesoCuenta()
        print("DNI:"); dni = input()
        cursor.execute("SELECT count(*) FROM usuarios WHERE dni = '" + dni + "'")
        res_dni = cursor.fetchall()

    print()
    print("Contraseña:"); password = input()
    cursor.execute("SELECT contraseña FROM usuarios WHERE dni = '" + dni + "'")
    res_password = cursor.fetchall()

    while res_password[0][0] != password:
        os.system('clear')
        print("La contraseña es incorrecta"); 
        print()

        LetreroAccesoCuenta()
        print("DNI:"); print(dni)
        print()
        print("Contraseña:"); password = input()
        cursor.execute("SELECT contraseña FROM usuarios WHERE dni = '" + dni + "'")
        res_password = cursor.fetchall()
   
    os.system('clear')

# -------------------------------------------------------------------------------------------------
# EJECUCIÓN DE LOS MENÚS
# -------------------------------------------------------------------------------------------------

def EjecucionMenuLogin():
    MenuLogin()
    res_login = input()
    
    while res_login != "4":
        os.system('clear')

        if res_login == "1":
            ComprobacionLogin()            
            EjecucionMenuPrincipal()  
        
        elif res_login == "2":
            CreacionCuentaCliente()
            EjecucionMenuPrincipal()

        elif res_login == "3":
            CreacionCuentaPeluquero()
            EjecucionMenuPrincipal()

        else:
            print(mensaje_error_seleccion)

        MenuLogin()
        res_login = input()

def EjecucionMenuPrincipal():
    MenuPrincipal()
    res_principal = input()
    os.system('clear')

    while res_principal != "8":
        os.system('clear')

        if res_principal == "1":
            EjecucionMenuPerfil()

        elif res_principal == "2":
            print("Veo listado de peluqueros")

        elif res_principal == "3":
            EjecucionMenuCitas()

        elif res_principal == "4":
            EjecucionMenuMensajes()

        elif res_principal == "5":
            EjecucionMenuValoraciones()

        elif res_principal == "6":
            print("Creo incidencia")

        elif res_principal == "7":
            EjecucionMenuAlmacen()

        else:
            print(mensaje_error_seleccion)

        MenuPrincipal()
        res_principal = input()
        if res_principal == "8":
            os.system('clear')

def EjecucionMenuPerfil():
    MenuPerfil()
    res_perfil = input()
    os.system('clear')

    while res_perfil != "4":
        os.system('clear')

        if res_perfil == "1":
            print("Veo mi perfil")

        elif res_perfil == "2":
            print("Modifico mi perfil")

        elif res_perfil == "3":
            print("Elimino mi perfil")

        else:
            print(mensaje_error_seleccion)

        MenuPerfil()
        res_perfil = input()
        if res_perfil == "4":
            os.system('clear')

def EjecucionMenuCitas():
    MenuCitas()
    res_citas = input()
    os.system('clear')

    while res_citas != "5":
        os.system('clear')

        if res_citas == "1":
            print("Veo mis citas")

        elif res_citas == "2":
            print("Creo una cita")

        elif res_citas == "3":
            print("Elimino una cita ")

        elif res_citas == "4":
            print("Modifico una cita ")

        else:
            print(mensaje_error_seleccion)

        MenuCitas()
        res_citas = input()
        if res_citas == "5":
            os.system('clear')

def EjecucionMenuMensajes():
    MenuMensajes()
    res_mensajes = input()
    os.system('clear')

    while res_mensajes != "3":
        os.system('clear')

        if res_mensajes == "1":
            print("Escribo mensaje")

        elif res_mensajes == "2":
            print("Elimino mensaje")

        else:
            print(mensaje_error_seleccion)

        MenuMensajes()
        res_mensajes = input()
        if res_mensajes == "3":
            os.system('clear')

def EjecucionMenuValoraciones():
    MenuValoraciones()
    res_valoraciones = input()
    os.system('clear')

    while res_valoraciones != "4":
        os.system('clear')

        if res_valoraciones == "1":
            print("Añado valoración")

        elif res_valoraciones == "2":
            print("Añado comentario")

        elif res_valoraciones == "3":
            print("Añado foto")

        else:
            print(mensaje_error_seleccion)

        MenuValoraciones()
        res_valoraciones = input()
        if res_valoraciones == "4":
            os.system('clear')

def EjecucionMenuAlmacen():
    MenuAlmacen()
    res_almacen = input()
    os.system('clear')

    while res_almacen != "4":
        os.system('clear')

        if res_almacen == "1":
            print("Creo almacen")

        elif res_almacen == "2":
            print("Encargo productos")

        elif res_almacen == "3":
            print("Elimino almacen")

        else:
            print(mensaje_error_seleccion)

        MenuAlmacen()
        res_almacen = input()
        if res_almacen == "4":
            os.system('clear')

# -------------------------------------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------------------------------------

try:
    mi_host         = "oracle0.ugr.es"
    mi_service_name = "practbd.oracle0.ugr.es"
    mi_port         = "1521"
    mi_dsn          = mi_host + ":" + mi_port + "/" + mi_service_name
    mi_user         = "x7555876"
    mi_password     = "x7555876"

    # creamos la conexión al SGBD
    conexion = cx_Oracle.connect(
        dsn=mi_dsn,
        user=mi_user,
        password=mi_password
    )
    
    os.system('clear')
    print("Se ha establecido la conexión con el SGBD")  
    print()

    # creamos el cursor
    cursor = conexion.cursor()

    # mensajes de error
    mensaje_error_seleccion = "Valor incorrecto introducido !"

    EjecucionMenuLogin()

    # cerramos la conexión con el SGBD
    conexion.close()
    print("Conexión finalizada")

except Exception as err:
    print("Error: ", err)
