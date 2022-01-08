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
# DECLARACIONES DE LOS MENÚS
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
    print("3.- Eliminar Perfil")
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
    print("1.- Leer mensajes")
    print("2.- Escribir un mensaje")
    print("3.- Eliminar un mensaje")
    print("4.- Volver atrás")
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

def LetreroPeluqueros():
    print("\t------------------------------")
    print("\t|   PELUQUEROS DISPONIBLES   |")
    print("\t------------------------------")
    print()

def LetreroPerfil():
    print("\t-------------------------")
    print("\t|   PERFIL DE USUARIO   |")
    print("\t-------------------------")
    print()

def LetreroMensajes():
    print("\t----------------")
    print("\t|   MENSAJES   |")
    print("\t----------------")
    print()

# -------------------------------------------------------------------------------------------------
# FUNCIONES DEL MENÚ LOGIN
# -------------------------------------------------------------------------------------------------

def ComprobacionLogin():
    LetreroAccesoCuenta()
    print("DNI:"); dni = input()
    cursor.execute("SELECT count(*) FROM usuarios WHERE dni = '" + dni + "'")
    res_dni = cursor.fetchall()

    while res_dni[0][0] == 0:
        os.system('clear')
        print(mensaje_NO_existe_usuario) 
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
        print(mensaje_wrong_password)
        print()

        LetreroAccesoCuenta()
        print("DNI:"); print(dni)
        print()
        print("Contraseña:"); password = input()
        cursor.execute("SELECT contraseña FROM usuarios WHERE dni = '" + dni + "'")
        res_password = cursor.fetchall()
    
    os.system('clear')
    return dni

def CreacionCuentaUsuario(valor):
    print("DNI:"); dni = input()
    cursor.execute("SELECT count(*) FROM usuarios WHERE dni = '" + dni + "'")
    res_dni = cursor.fetchall()
    
    while res_dni[0][0] != 0:
        os.system('clear')
        print(mensaje_existe_usuario_DNI)
        print()

        LetreroCreacionCuentaCliente()
        print("DNI:"); dni = input()
        cursor.execute("SELECT count(*) FROM usuarios WHERE dni = '" + dni + "'")
        res_dni = cursor.fetchall()

    valores = LecturaDatos()
    cursor.execute("INSERT INTO usuarios VALUES ('" + dni + "', '" + valores[0] + "', '" + valores[1] + "', '" + valores[2] + "', TO_DATE('" + valores[3] + "', 'DD/MM/YYYY'), '" + valores[4] + "', '" + str(valor) + "')")

    # jjj no se si es necesario el commit
    cursor.execute("COMMIT")
    return dni

def CreacionCuentaCliente():
    LetreroCreacionCuentaCliente()
    dni = CreacionCuentaUsuario(0)
    cursor.execute("INSERT INTO clientes VALUES ('" + dni + "')")
    
    # jjj no se si es necesario el commit
    cursor.execute("COMMIT")
    os.system('clear')
    return dni

def CreacionCuentaPeluquero():
    LetreroCreacionCuentaPeluquero()
    dni = CreacionCuentaUsuario(1)

    print("CNAE:");                 cnae = input()
    print("Localización:"); localizacion = input()
    cursor.execute("INSERT INTO peluqueros VALUES ('" + dni + "', '" + cnae + "', '" + localizacion + "')")
    
    # jjj no se si es necesario el commit
    cursor.execute("COMMIT")
    os.system('clear')
    return dni

# -------------------------------------------------------------------------------------------------
# FUNCIONES DEL MENÚ PRINCIPAL
# -------------------------------------------------------------------------------------------------

def VisualizarPeluqueros():
    LetreroPeluqueros()
    cursor.execute("SELECT dni, username FROM usuarios WHERE es_cliente = '1'")
    lista_peluqueros = cursor.fetchall()

    for peluquero in lista_peluqueros:
        print("Peluquero : " + peluquero[1] + ", con dni : " + peluquero[0])

    input()
    os.system('clear')

# -------------------------------------------------------------------------------------------------
# FUNCIONES DEL MENÚ PERFIL
# -------------------------------------------------------------------------------------------------

def VisualizarPerfil(dni):
    LetreroPerfil()
    cursor.execute("SELECT * FROM usuarios where dni = '" + dni + "'")
    info = cursor.fetchall()

    cursor.execute("SELECT es_cliente FROM usuarios where dni = '" + dni + "'")
    es_cliente = cursor.fetchall()
    
    if es_cliente[0][0] == 0:
        tipo_usuario = "Cliente"
    else:
        tipo_usuario = "Peluquero"

    print("DNI                : " + info[0][0])
    print("Nombre de usuario  : " + info[0][1])
    print("Contraseña         : " + info[0][2])
    print("Nombre y Apellidos : " + info[0][3])
    print("Fecha Nacimiento   : " + str(info[0][4]))
    print("Correo electrónico : " + info[0][5])
    print("Tipo de usuario    : " + tipo_usuario)
    
    if es_cliente[0][0] == 1:
        cursor.execute("SELECT * FROM peluqueros where dni = '" + dni + "'")
        info_pelu = cursor.fetchall()
        print("CNAE               : " + info_pelu[0][1])
        print("Localización       : " + info_pelu[0][2])

    input()
    os.system('clear')

def ModificarPerfil(dni):
    LetreroPerfil()
    cursor.execute("SELECT es_cliente FROM usuarios where dni = '" + dni + "'")
    es_cliente = cursor.fetchall()
    valores = LecturaDatos()

    if es_cliente[0][0] == 0:
        cursor.execute("DELETE FROM clientes WHERE dni = '" + dni + "'")
        cursor.execute("DELETE FROM usuarios WHERE dni = '" + dni + "'")
    else:
        cursor.execute("DELETE FROM peluqueros WHERE dni = '" + dni + "'")
        cursor.execute("DELETE FROM usuarios WHERE dni = '" + dni + "'")

    cursor.execute("INSERT INTO usuarios VALUES ('" + dni + "', '" + valores[0] + "', '" + valores[1] + "', '" + valores[2] + "', TO_DATE('" + valores[3] + "', 'DD/MM/YYYY'), '" + valores[4] + "', '" + str(es_cliente[0][0]) + "')")

    if es_cliente[0][0] == 0:    
        cursor.execute("INSERT INTO clientes VALUES ('" + dni + "')")
    else:
        print("CNAE:");                 cnae = input()
        print("Localización:"); localizacion = input()
        cursor.execute("INSERT INTO peluqueros VALUES ('" + dni + "', '" + cnae + "', '" + localizacion + "')")

    # jjj no se si es necesario el commit
    cursor.execute("COMMIT")
    os.system('clear')

def EliminarPerfil(dni):
    cursor.execute("SELECT es_cliente FROM usuarios WHERE dni = '" + dni + "'")
    es_cliente = cursor.fetchall()

    if es_cliente[0][0] == 0:
        print(mensaje_es_cliente_No_elimina_cuenta)
    
    else:
        cursor.execute("DELETE FROM peluqueros WHERE dni = '" + dni + "'")
        cursor.execute("DELETE FROM usuarios WHERE dni = '" + dni + "'")
        # jjj no se si es necesario el commit
        cursor.execute("COMMIT")
        os.system('clear')
        print(mensaje_eliminacion_cuenta + " " + dni)

# -------------------------------------------------------------------------------------------------
# FUNCIONES DEL MENÚ MENSAJES
# -------------------------------------------------------------------------------------------------

def EscribirMensaje(dni):
    LetreroMensajes()
    print("DNI del destinatario : "); dni_destinatario = input(); print()
    cursor.execute("SELECT count(*) FROM usuarios WHERE dni = '" + dni_destinatario + "'")
    existe_destinatario = cursor.fetchall()
    
    while existe_destinatario[0][0] == 0:
        os.system('clear')
        print(mensaje_NO_existe_usuario)
        print()

        LetreroMensajes()
        print("DNI del destinatario : "); dni_destinatario = input(); print()
        cursor.execute("SELECT count(*) FROM usuarios WHERE dni = '" + dni_destinatario + "'")
        existe_destinatario = cursor.fetchall()

    print("Identificador del mensaje : "); id_men = input(); print()
    cursor.execute("SELECT count(*) FROM mensajes WHERE id_mensaje = '" + id_men + "'")
    existe_id_men = cursor.fetchall()
    
    while existe_id_men[0][0] != 0:
        os.system('clear')
        print(mensaje_id_men_ya_existe)
        print()

        LetreroMensajes()
        print("DNI del destinatario : "); print(dni_destinatario); print()
        print("Identificador del mensaje : "); id_men = input(); print()
        cursor.execute("SELECT count(*) FROM mensajes WHERE id_mensaje = '" + id_men + "'")
        existe_id_men = cursor.fetchall()

    print("Mensaje : "); contenido_men = input(); print()

    cursor.execute("INSERT INTO mensajes VALUES ('" + id_men + "', '" + dni + "', '" + dni_destinatario + "', '" + contenido_men + "')")
    
    # jjj no se si es necesario el commit
    cursor.execute("COMMIT")
    os.system('clear')
    print(mensaje_men_enviado)

def VisualizarMensajes(dni):
    LetreroMensajes() 
    cursor.execute("SELECT * FROM mensajes")
    mensajes = cursor.fetchall()
    
    for mensaje in mensajes:
        if mensaje[1] == dni:
            print(dni + " : " + mensaje[3])
        if mensaje[2] == dni:
            print("\t\t\t\t\t" + dni + " : " + mensaje[3])

    input()
    os.system('clear')

# -------------------------------------------------------------------------------------------------
# FUNCIONES ADICIONALES 
# -------------------------------------------------------------------------------------------------

def LecturaDatos():
    print("Nombre usuario:");       nombre_usuario = input()
    print("Contraseña:");                 password = input()
    print("Nombre y Apellidos:"); nombre_apellidos = input()
    print("Fecha Nacimiento:");              fecha = input()
    print("Correo electrónico:");           correo = input()

    resultado = [nombre_usuario, password, nombre_apellidos, fecha, correo]
    return resultado

# -------------------------------------------------------------------------------------------------
# EJECUCIÓN DE LOS MENÚS
# -------------------------------------------------------------------------------------------------

def EjecucionMenuLogin():
    MenuLogin()
    res_login = input()
    
    while res_login != "4":
        os.system('clear')

        if res_login == "1":
            dni = ComprobacionLogin()            
            EjecucionMenuPrincipal(dni)  
        
        elif res_login == "2":
            dni = CreacionCuentaCliente()
            EjecucionMenuPrincipal(dni)

        elif res_login == "3":
            dni = CreacionCuentaPeluquero()
            EjecucionMenuPrincipal(dni)

        else:
            print(mensaje_error_seleccion)

        MenuLogin()
        res_login = input()

def EjecucionMenuPrincipal(dni):
    MenuPrincipal()
    res_principal = input()
    os.system('clear')

    while res_principal != "8":
        os.system('clear')

        if res_principal == "1":
            EjecucionMenuPerfil(dni)
            
            # si se ha eliminado el perfil, salimos al Menu Login
            cursor.execute("SELECT count(*) FROM usuarios WHERE dni = '" + dni + "'")
            existe_dni = cursor.fetchall()

            if existe_dni[0][0] == 0:
                return

        elif res_principal == "2":
            VisualizarPeluqueros()

        elif res_principal == "3":
            EjecucionMenuCitas(dni)

        elif res_principal == "4":
            EjecucionMenuMensajes(dni)

        elif res_principal == "5":
            EjecucionMenuValoraciones(dni)

        elif res_principal == "6":
            print("Creo incidencia")

        elif res_principal == "7":
            EjecucionMenuAlmacen(dni)

        else:
            print(mensaje_error_seleccion)

        MenuPrincipal()
        res_principal = input()
        if res_principal == "8":
            os.system('clear')
    
    if res_principal == "8":
        print(mensaje_cerrar_sesion)

def EjecucionMenuPerfil(dni):
    MenuPerfil()
    res_perfil = input()
    os.system('clear')

    while res_perfil != "4":
        os.system('clear')

        if res_perfil == "1":
            VisualizarPerfil(dni)

        elif res_perfil == "2":
            ModificarPerfil(dni)

        elif res_perfil == "3":
            EliminarPerfil(dni)
            break

        else:
            print(mensaje_error_seleccion)

        MenuPerfil()
        res_perfil = input()
        if res_perfil == "4":
            os.system('clear')

def EjecucionMenuCitas(dni):
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

def EjecucionMenuMensajes(dni):
    MenuMensajes()
    res_mensajes = input()
    os.system('clear')

    while res_mensajes != "4":
        os.system('clear')

        if res_mensajes == "1":
            VisualizarMensajes(dni)

        elif res_mensajes == "2":
            EscribirMensaje(dni)

        elif res_mensajes == "3":
            print("Elimino mensaje")

        else:
            print(mensaje_error_seleccion)

        MenuMensajes()
        res_mensajes = input()
        if res_mensajes == "4":
            os.system('clear')

def EjecucionMenuValoraciones(dni):
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

def EjecucionMenuAlmacen(dni):
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
    mensaje_error_seleccion              = "Valor incorrecto introducido !"
    mensaje_existe_usuario_DNI           = "Ya existe un usuario con ese DNI"
    mensaje_NO_existe_usuario            = "No existe este usuario"
    mensaje_wrong_password               = "La contraseña es incorrecta"
    mensaje_es_cliente_No_elimina_cuenta = "Solo los peluqueros pueden eliminar su cuenta"
    mensaje_eliminacion_cuenta           = "Se ha eliminado la cuenta con DNI"
    mensaje_cerrar_sesion                = "Se ha cerrado la sesión"
    mensaje_men_enviado                  = "Mensaje enviado correctamente"
    mensaje_id_men_ya_existe             = "Este identificador ya está en uso"
    
    EjecucionMenuLogin()

    # cerramos la conexión con el SGBD
    conexion.close()
    print("Conexión finalizada")

except Exception as err:
    print("Error: ", err)
