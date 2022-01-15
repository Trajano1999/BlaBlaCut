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
# VARIABLES GLOBALES
# -------------------------------------------------------------------------------------------------

id_men_global = 0

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

def MenuEleccionCuenta():
    print()
    print("0.- Cuenta Cliente")
    print("1.- Cuenta Peluquero")
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
    print()
    print("1.- Perfil")
    print("2.- Ver listado de Peluqueros")
    print("3.- Citas")                                                                             # consumir producto en cita
    print("4.- Mensajes")
    print("5.- Valoraciones")
    print("6.- Almacén")
    print("7.- Cerrar Sesión")
    print()

def MenuPerfilCliente():
    print()
    print("1.- Modificar Perfil")
    print("2.- Volver atrás")
    print()

def MenuPerfilPeluquero():
    print()
    print("1.- Modificar Perfil")
    print("2.- Eliminar Perfil")
    print("3.- Volver atrás")
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
    print("1.- Añadir valoración y comentario")
    print("2.- Añadir fotorafía")
    print("3.- Añadir incidencia")
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

def LetreroConexionBaseDatos():
    print()
    print("\t------------------------")
    print("\t|   CONEXIÓN AL SGBD   |")
    print("\t------------------------")
    print()

def LetreroAccesoCuenta():
    print("\t--------------------------")
    print("\t|   ACCESO A LA CUENTA   |")
    print("\t--------------------------")
    print()

def LetreroEleccionCuenta():
    print("\t-----------------------------")
    print("\t|   ELECCIÓN DE LA CUENTA   |")
    print("\t-----------------------------")
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

def EleccionCuenta(dni):
    cursor.execute("SELECT count(*) FROM clientes WHERE dni = '" + dni + "'")
    es_cliente = cursor.fetchall()
    cursor.execute("SELECT count(*) FROM peluqueros WHERE dni = '" + dni + "'")
    es_peluquero = cursor.fetchall()

    if es_cliente[0][0] != 0 and es_peluquero[0][0] == 0:
        return 0

    elif es_cliente[0][0] == 0 and es_peluquero[0][0] != 0:
        return 1

    elif es_cliente[0][0] != 0 and es_peluquero[0][0] != 0:
        LetreroEleccionCuenta()
        MenuEleccionCuenta()
        respuesta = input()

        while respuesta != "0" and respuesta != "1":
            LetreroEleccionCuenta()
            MenuEleccionCuenta()
            respuesta = input()
        
        os.system('clear')
        return respuesta

def CreacionCuentaCliente():
    LetreroCreacionCuentaCliente()
    print("DNI:"); dni = input(); print()

    cursor.execute("SELECT count(*) FROM usuarios WHERE dni = '" + dni + "'")
    res_dni = cursor.fetchall()
    cursor.execute("SELECT count(*) FROM clientes WHERE dni = '" + dni + "'")
    es_cliente = cursor.fetchall()

    while res_dni[0][0] != 0 and es_cliente[0][0] != 0:
        os.system('clear')
        print(mensaje_existe_cliente)
        print()
        
        LetreroCreacionCuentaCliente()
        print("DNI:"); dni = input(); print()
        cursor.execute("SELECT count(*) FROM usuarios WHERE dni = '" + dni + "'")
        res_dni = cursor.fetchall()
        cursor.execute("SELECT count(*) FROM clientes WHERE dni = '" + dni + "'")
        es_cliente = cursor.fetchall()

    valores = LecturaDatos()

    if res_dni[0][0] == 0:
        cursor.execute("INSERT INTO usuarios VALUES ('" + dni + "', '" + valores[0] + "', '" + valores[1] + "', '" + valores[2] + "', TO_DATE('" + valores[3] + "', 'DD/MM/YYYY'), '" + valores[4] + "')")
    
    cursor.execute("INSERT INTO clientes VALUES ('" + dni + "')")
    cursor.execute("COMMIT")
    os.system('clear')
    return dni

def CreacionCuentaPeluquero():
    LetreroCreacionCuentaPeluquero()
    print("DNI:"); dni = input(); print()

    cursor.execute("SELECT count(*) FROM usuarios WHERE dni = '" + dni + "'")
    res_dni = cursor.fetchall()
    cursor.execute("SELECT count(*) FROM peluqueros WHERE dni = '" + dni + "'")
    es_peluquero = cursor.fetchall()

    while res_dni[0][0] != 0 and es_peluquero[0][0] != 0:
        os.system('clear')
        print(mensaje_existe_peluquero)
        print()
        
        LetreroCreacionCuentaPeluquero()
        print("DNI:"); dni = input(); print()
        cursor.execute("SELECT count(*) FROM usuarios WHERE dni = '" + dni + "'")
        res_dni = cursor.fetchall()
        cursor.execute("SELECT count(*) FROM peluqueros WHERE dni = '" + dni + "'")
        es_peluquero = cursor.fetchall()

    valores = LecturaDatos()
    print("CNAE:");                 cnae = input(); print()
    print("Localización:"); localizacion = input(); print()

    if res_dni[0][0] == 0:
        cursor.execute("INSERT INTO usuarios VALUES ('" + dni + "', '" + valores[0] + "', '" + valores[1] + "', '" + valores[2] + "', TO_DATE('" + valores[3] + "', 'DD/MM/YYYY'), '" + valores[4] + "')")
        
    cursor.execute("INSERT INTO peluqueros VALUES ('" + dni + "', '" + cnae + "', '" + localizacion + "')")
    cursor.execute("COMMIT")
    os.system('clear')
    return dni

# -------------------------------------------------------------------------------------------------
# FUNCIONES DEL MENÚ PRINCIPAL
# -------------------------------------------------------------------------------------------------

def VisualizarPeluqueros():
    LetreroPeluqueros()
    cursor.execute("SELECT dni, username FROM peluqueros NATURAL JOIN usuarios")
    lista_peluqueros = cursor.fetchall()

    for peluquero in lista_peluqueros:
        print("Peluquero con dni : " + peluquero[0] + " y nombre : " + peluquero[1])

    input()
    os.system('clear')

# -------------------------------------------------------------------------------------------------
# FUNCIONES DEL MENÚ PERFIL
# -------------------------------------------------------------------------------------------------

def ModificarPerfil(dni, tipo_cuenta):
    LetreroPerfil()
    valores = LecturaDatos()

    cursor.execute("UPDATE usuarios SET username = '" + valores[0] + "', contraseña = '" + valores[1] + "', nombre = '" + valores[2] + "', fecha_nacimiento = TO_DATE('" + valores[3] + "', 'DD/MM/YYYY'), correo = '" + valores[4] + "'  WHERE dni = '" + dni + "'")

    if tipo_cuenta == 1:
        print("CNAE:");                 cnae = input(); print()
        print("Localización:"); localizacion = input(); print()
        cursor.execute("UPDATE peluqueros SET cnae = '" + cnae + "', localizacion = '" + localizacion + "' where dni = '" + dni + "'")

    cursor.execute("COMMIT")
    os.system('clear')

def EliminarPerfil(dni):
    cursor.execute("SELECT count(*) FROM clientes WHERE dni = '" + dni + "'")
    es_cliente = cursor.fetchall()

    cursor.execute("DELETE FROM peluqueros WHERE dni = '" + dni + "'")

    if es_cliente[0][0] == 0:
        cursor.execute("DELETE FROM usuarios WHERE dni = '" + dni + "'")
  
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

    global id_men_global
    cursor.execute("SELECT count(*) FROM mensajes WHERE id_mensaje = '" + str(id_men_global) + "'")
    existe_id_men = cursor.fetchall()
    
    while existe_id_men[0][0] != 0:
        id_men_global += 1
        cursor.execute("SELECT count(*) FROM mensajes WHERE id_mensaje = '" + str(id_men_global) + "'")
        existe_id_men = cursor.fetchall()

    print("Mensaje : "); contenido_men = input(); print()
    cursor.execute("INSERT INTO mensajes VALUES ('" + str(id_men_global) + "', '" + dni + "', '" + dni_destinatario + "', '" + contenido_men + "')")
    
    cursor.execute("COMMIT")
    os.system('clear')
    print(mensaje_men_enviado)

def EliminarMensaje(dni):
    LetreroMensajes()
    print("Identificador del mensaje a eliminar : "); id_men = input(); print()
    cursor.execute("SELECT emisor FROM mensajes WHERE id_mensaje = '" + id_men + "'")
    emisor = cursor.fetchall()

    if emisor[0][0] == dni:
        cursor.execute("DELETE FROM mensajes WHERE id_mensaje = '" + id_men + "'")
        cursor.execute("COMMIT")
    else:
        print(mensaje_emisor_incorrecto)

    os.system('clear')
    print(mensaje_eliminado)
    
# -------------------------------------------------------------------------------------------------
# FUNCIONES ADICIONALES 
# -------------------------------------------------------------------------------------------------

def LecturaDatos():
    print("Nombre usuario:");       nombre_usuario = input(); print()
    print("Contraseña:");                 password = input(); print()
    print("Nombre y Apellidos:"); nombre_apellidos = input(); print()
    print("Fecha Nacimiento:");              fecha = input(); print()
    print("Correo electrónico:");           correo = input(); print()

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
            EjecucionMenuPrincipal(dni, int(EleccionCuenta(dni)))  
        
        elif res_login == "2":
            dni = CreacionCuentaCliente()
            EjecucionMenuPrincipal(dni, int(0))

        elif res_login == "3":
            dni = CreacionCuentaPeluquero()
            EjecucionMenuPrincipal(dni, int(1))

        else:
            print(mensaje_error_seleccion)

        MenuLogin()
        res_login = input()

def EjecucionMenuPrincipal(dni, tipo_cuenta):
    MenuPrincipal()
    res_principal = input()
    os.system('clear')

    while res_principal != "7":
        os.system('clear')

        if res_principal == "1":
            resultado = EjecucionMenuPerfil(dni, tipo_cuenta)
            
            # si se ha eliminado el perfil de peluquero, salimos al Menu Login (el perfil de cliente sigue existiendo)
            if resultado == 1:
                break

        elif res_principal == "2":
            VisualizarPeluqueros()

        elif res_principal == "3":
            EjecucionMenuCitas(dni, tipo_cuenta)

        elif res_principal == "4":
            EjecucionMenuMensajes(dni)

        elif res_principal == "5":
            EjecucionMenuValoraciones(dni, tipo_cuenta)

        elif res_principal == "6":
            EjecucionMenuAlmacen(dni, tipo_cuenta)

        else:
            print(mensaje_error_seleccion)

        MenuPrincipal()
        res_principal = input()
        if res_principal == "7":
            os.system('clear')
    
    if res_principal == "7":
        print(mensaje_cerrar_sesion)

def EjecucionMenuPerfil(dni, tipo_cuenta):
    if tipo_cuenta == 0:
        MenuPerfilCliente()
        res_perfil_cliente = input()
        os.system('clear')
        
        while res_perfil_cliente != "2":
            os.system('clear')

            if res_perfil_cliente == "1":
                ModificarPerfil(dni, tipo_cuenta)

            else:
                print(mensaje_error_seleccion)

            MenuPerfilCliente()
            res_perfil_cliente = input()
            if res_perfil_cliente == "2":
                os.system('clear')
    else:
        MenuPerfilPeluquero()
        res_perfil_peluquero = input()
        os.system('clear')

        while res_perfil_peluquero != "3":
            os.system('clear')

            if res_perfil_peluquero == "1":
                ModificarPerfil(dni,tipo_cuenta)

            elif res_perfil_peluquero == "2":
                EliminarPerfil(dni)
                return 1

            else:
                print(mensaje_error_seleccion)

            MenuPerfilPeluquero()
            res_perfil_peluquero = input()
            if res_perfil_peluquero == "3":
                os.system('clear')
    
    return 0

def EjecucionMenuCitas(dni, tipo_cuenta):
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

    while res_mensajes != "3":
        os.system('clear')

        if res_mensajes == "1":
            EscribirMensaje(dni)

        elif res_mensajes == "2":
            EliminarMensaje(dni)

        else:
            print(mensaje_error_seleccion)

        MenuMensajes()
        res_mensajes = input()
        if res_mensajes == "3":
            os.system('clear')

def EjecucionMenuValoraciones(dni, tipo_cuenta):
    MenuValoraciones()
    res_valoraciones = input()
    os.system('clear')

    while res_valoraciones != "4":
        os.system('clear')

        if res_valoraciones == "1":
            print("Añado valoración y comentario")

        elif res_valoraciones == "2":
            print("Añado foto")

        elif res_valoraciones == "3":
            print("Añado incidencia")

        else:
            print(mensaje_error_seleccion)

        MenuValoraciones()
        res_valoraciones = input()
        if res_valoraciones == "4":
            os.system('clear')

def EjecucionMenuAlmacen(dni, tipo_cuenta):
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
    # mensajes de error
    mensaje_error_seleccion    = "Valor incorrecto introducido !"
    mensaje_wrong_password     = "La contraseña es incorrecta"
    
    # mensajes de usuarios
    mensaje_existe_cliente     = "Ya existe un cliente con ese DNI"
    mensaje_existe_peluquero   = "Ya existe un peluquero con ese DNI"
    mensaje_NO_existe_usuario  = "No existe este usuario"
    mensaje_eliminacion_cuenta = "Se ha eliminado la cuenta con DNI"
    mensaje_cerrar_sesion      = "Se ha cerrado la sesión"
    
    # mensajes de mensajes
    mensaje_men_enviado        = "Mensaje enviado correctamente"
    mensaje_eliminado          = "Mensaje eliminado correctamente"
    mensaje_id_men_ya_existe   = "Este identificador ya está en uso"
    mensaje_emisor_incorrecto  = "No es posible eliminar mensajes de otros usuarios"

    # petición de los datos para la conexion al SGBD
    os.system('clear')
    LetreroConexionBaseDatos()

    print("Host : "); mi_host = input()
    if mi_host == "":
        mi_host = "oracle0.ugr.es"

    print("Sid : "); mi_sid_inicial = input()
    if mi_sid_inicial == "":
        mi_sid_inicial = "practbd"

    print("Puerto : "); mi_port = input()
    if mi_port == "":
        mi_port = "1521"

    print("Usuario : "); mi_user = input()
    if mi_user == "":
        mi_user = "x7555876"

    print("Contraseña : "); mi_password = input()
    if mi_password == "":
        mi_password = "x7555876"
    
    mi_sid = mi_sid_inicial + "." + mi_host
    mi_dsn = mi_host + ":" + mi_port + "/" + mi_sid

    # creación de la conexión al SGBD
    conexion = cx_Oracle.connect(
        dsn=mi_dsn,
        user=mi_user,
        password=mi_password
    )
    
    os.system('clear')
    print("Se ha establecido la conexión con el SGBD")  
    print()

    # creación del cursor
    cursor = conexion.cursor()
    
    EjecucionMenuLogin()

    # cierre de la conexión con el SGBD
    conexion.close()
    print("Conexión finalizada")

except Exception as err:
    print("Error: ", err)
