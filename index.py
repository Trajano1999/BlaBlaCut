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
    print("3.- Citas")                                                                             # consumir prodcuto en cita
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
# CREACION DE LAS CUENTAS
# -------------------------------------------------------------------------------------------------

def CreacionCuentaCliente():
    print("\t----------------------------------")
    print("\t|   CREACIÓN DE CUENTA CLIENTE   |")
    print("\t----------------------------------")
    print()
    print("Nombre usuario:");     nombre_usuario_cliente   = input()
    print("Contraseña:");         password_cliente         = input()
    print("Nombre y Apellidos:"); nombre_apellidos_cliente = input()
    print("DNI:");                dni_cliente              = input()
    print("Fecha Nacimiento:");   fecha_cliente            = input()
    print("Correo electrónico:"); correo_cliente           = input()
    os.system('clear')

def CreacionCuentaPeluquero():
    print("\t------------------------------------")
    print("\t|   CREACIÓN DE CUENTA PELUQUERO   |")
    print("\t------------------------------------")
    print()
    print("Nombre usuario:");     nombre_usuario_peluquero   = input()
    print("Contraseña:");         password_peluquero         = input()
    print("Nombre y Apellidos:"); nombre_apellidos_peluquero = input()
    print("DNI:");                dni_peluquero              = input()
    print("Fecha Nacimiento:");   fecha_peluquero            = input()
    print("Correo electrónico:"); correo_peluquero           = input()
    print("CNAE:");               cnae_peluquero             = input()
    print("Localización:");       localizacion_peluquero     = input()
    os.system('clear')

# -------------------------------------------------------------------------------------------------
# FUNCIONES ADICIONALES
# -------------------------------------------------------------------------------------------------

def ComprobacionLogin():
    print("\t--------------------------")
    print("\t|   ACCESO A LA CUENTA   |")
    print("\t--------------------------")
    print()
    print("Usuario:");    usuario  = input()
    print("Contraseña:"); password = input()
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

    # conexión al SGBD
    conexion = cx_Oracle.connect(
        dsn=mi_dsn,
        user=mi_user,
        password=mi_password
    )
    
    print()
    print("Se ha establecido la conexión")  

    # mensajes de error
    mensaje_error_seleccion = "Valor incorrecto introducido !"

    os.system('clear')
    EjecucionMenuLogin()

    # cerramos la conexión con el SGBD
    print("Cerrando la conexión...")
    conexion.close()

except Exception as err:
    print("Error: ", err)
