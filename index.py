# -------------------------------------------------------------------------------------------------
#  
#   SEMINARIO 1 
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

import pyodbc
import os                                                                                          # para limpiar la consola

# -------------------------------------------------------------------------------------------------
# MENÚS
# ----------------- --------------------------------------------------------------------------------

def MostrarIndice():
    print()
    print("------------------------")
    print("|    MENU PRINCIPAL    |")
    print("------------------------")

    print("1.- Mostrar todas las tablas.")
    print("2.- Crear una tabla.")
    print("3.- Mostrar una tabla.")
    print("4.- Eliminar una tabla.")
    print("5.- Añadir tuplas en Stock.")
    print("6.- Dar de alta nuevo pedido.")
    print("7.- Desconectar de la base de datos.")
    print()

def ElegirTablas():
    print()
    print("Elige una tabla :")
    print("1.- Stock")
    print("2.- Pedido")
    print("3.- DetallePedido")
    print("4.- Volver atrás")
    print()

def MenuDardeAlta():
    print()
    print("Elige una opción :")
    print("1.- Añadir detalle de producto")
    print("2.- Eliminar todos los detalles de producto")
    print("3.- Cancelar producto")
    print("4.- Finalizar pedido")
    print()

# -------------------------------------------------------------------------------------------------
# AÑADIR TABLAS
# -------------------------------------------------------------------------------------------------

def AñadirStock():
    cursor.execute("create table Stock(                                                            \
        Cproducto INT PRIMARY KEY,                                                                 \
        Cantidad INT NOT NULL                                                                      \
    )")
    cursor.execute("COMMIT")
    print("Se ha creado la tabla Stock")

def AñadirPedido():
    cursor.execute("create table Pedido(                                                           \
        Cpedido INT PRIMARY KEY,                                                                   \
        Ccliente INT NOT NULL,                                                                     \
        FechaPedido DATE NOT NULL                                                                  \
    )")
    cursor.execute("COMMIT")
    print("Se ha creado la tabla Pedido")

def AñadirDetallePedido():
    cursor.execute("create table DetallePedido(                                                    \
        Cpedido INT REFERENCES Pedido(Cpedido),                                                    \
        Cproducto INT REFERENCES Stock(Cproducto),                                                 \
        Cantidad INT NOT NULL,                                                                     \
        PRIMARY KEY(Cpedido, Cproducto)                                                            \
    )")
    cursor.execute("COMMIT")
    print("Se ha creado la tabla DetallePedido")

# -------------------------------------------------------------------------------------------------
# CONSULTAR TABLAS
# -------------------------------------------------------------------------------------------------

def ConsultarTablas():
    cursor.execute("SELECT table_name FROM user_tables")
    consulta = cursor.fetchall()
    print("Las tablas del la BD son :", consulta)

def ConsultarLaTabla( nombre_tabla ):
    cursor.execute("SELECT * FROM " + nombre_tabla)
    consulta = cursor.fetchall()

    print("La tabla " + nombre_tabla + " es :")
    for i in consulta:
        print(i)

# -------------------------------------------------------------------------------------------------
# ELIMINAR TABLAS
# -------------------------------------------------------------------------------------------------

def EliminarLaTabla( nombre_tabla ):
    cursor.execute("DROP TABLE " + nombre_tabla)
    cursor.execute("COMMIT")
    print("Se ha eliminado la tabla " + nombre_tabla)

# -------------------------------------------------------------------------------------------------
# INSERTAR TUPLAS
# -------------------------------------------------------------------------------------------------

def InsertarValoresStock():
    cursor.execute("INSERT INTO Stock VALUES ('1','2')")
    cursor.execute("INSERT INTO Stock VALUES ('2','8')")
    cursor.execute("INSERT INTO Stock VALUES ('3','7')")
    cursor.execute("INSERT INTO Stock VALUES ('4','5')")
    cursor.execute("INSERT INTO Stock VALUES ('5','3')")
    cursor.execute("INSERT INTO Stock VALUES ('6','1')")
    cursor.execute("INSERT INTO Stock VALUES ('7','15')")
    cursor.execute("INSERT INTO Stock VALUES ('8','10')")
    cursor.execute("INSERT INTO Stock VALUES ('9','12')")
    cursor.execute("INSERT INTO Stock VALUES ('10','3')")
    cursor.execute("COMMIT")
    print("Se han insertado 10 tuplas en la tabla Stock")

def InsertarValoresDetallePedido( lec_cpedido ):
    print("Introduzca el Cproducto :")
    lec_cproducto = input()
    print("Introduzca la Cantidad :")
    lec_can = input()
    
    cursor.execute("INSERT INTO DetallePedido VALUES (?, ?, ?)", lec_cpedido, lec_cproducto, lec_can)
    os.system('clear')
    print("Se ha insertado correctamente en la tabla DetallePedido")
    ConsultarTablas()

def InsertarValoresPedido():
    cursor.execute("INSERT INTO Pedido VALUES (?, ?, TO_DATE( ?, 'DD/MM/YY'))", el_cpedido, el_ccliente, la_fecha)
    os.system('clear')
    print("Se ha insertado correctamente en la tabla Pedido")

# -------------------------------------------------------------------------------------------------
# CERRAR LA CONEXIÓN CON LA BD
# -------------------------------------------------------------------------------------------------

def CerrarConexion( conexion ):
    conexion.close()
    print()
    print("Conexión finalizada")
    print()

try: 
    conexion = pyodbc.connect('                                                                    \
        DRIVER={Devart ODBC Driver for Oracle};                                                    \
        Direct       = True;                                                                       \
        Host         = oracle0.ugr.es;                                                             \
        Service Name = practbd.oracle0.ugr.es;                                                     \
        User ID      = x7555876;                                                                   \
        Password     = x7555876')
    print()
    print("Se ha establecido la conexión")
    
    cursor = conexion.cursor()

    # codigos de mensaje
    mensaje_exito = "Se han guardado los cambios correctamente"
    mensaje_error = "Valor erroneo introducido !"
    mensaje_rol0 = "Se han borrado todos los detalles"
    mensaje_rol1 = "Se han borrado solo los detalles"

    # mostramos el Menu de la app
    MostrarIndice()
    ans = input()
    tabla = ans

    while ans != "7":
        os.system('clear')

        if ans == "1":
            ConsultarTablas()
            MostrarIndice()
            ans = input()

        elif ans == "2":
            ElegirTablas()
            tabla = input()

            while tabla != "4":
                os.system('clear')

                if tabla == "1":
                    AñadirStock()
                    ElegirTablas()
                    tabla = input()

                elif tabla == "2":
                    AñadirPedido()
                    ElegirTablas()
                    tabla = input()
                    
                elif tabla == "3":
                    AñadirDetallePedido()
                    ElegirTablas()
                    tabla = input()

                else:
                    print(mensaje_error)
                    ElegirTablas()
                    tabla = input()
                    
            os.system('clear')
            MostrarIndice()
            ans = input()

        elif ans == "3":
            ElegirTablas()
            tabla = input()

            while tabla != "4":
                os.system('clear')

                if tabla == "1":
                    ConsultarLaTabla("Stock")
                    ElegirTablas()
                    tabla = input()

                elif tabla == "2":
                    ConsultarLaTabla("Pedido")
                    ElegirTablas()
                    tabla = input()
                    
                elif tabla == "3":
                    ConsultarLaTabla("DetallePedido")
                    ElegirTablas()
                    tabla = input()

                else:
                    print(mensaje_error)
                    ElegirTablas()
                    tabla = input()
                    
            os.system('clear')
            MostrarIndice()
            ans = input()

        elif ans == "4":
            ElegirTablas()
            tabla = input()

            while tabla != "4":
                os.system('clear')

                if tabla == "1":
                    EliminarLaTabla("Stock")
                    ElegirTablas()
                    tabla = input()

                elif tabla == "2":
                    EliminarLaTabla("Pedido")
                    ElegirTablas()
                    tabla = input()
                    
                elif tabla == "3":
                    EliminarLaTabla("DetallePedido")
                    ElegirTablas()
                    tabla = input()

                else:
                    print(mensaje_error)
                    ElegirTablas()
                    tabla = input()
                    
            os.system('clear')
            MostrarIndice()
            ans = input()

        elif ans == "5":
            InsertarValoresStock()
            MostrarIndice()
            ans = input()

        elif ans == "6":
            cursor.execute("SAVEPOINT cero")
            
            print("Introduce los valores del Pedido.")
            print("Introduce el Cpedido :")
            el_cpedido = input()
            print("Introduce el Ccliente :")
            el_ccliente = input()
            print("Introduce la Fecha :")
            la_fecha = input()

            InsertarValoresPedido()
            cursor.execute("SAVEPOINT uno")

            MenuDardeAlta()
            opc = input()

            while opc != "4":
                os.system('clear')

                if opc == "1":
                    InsertarValoresDetallePedido(el_cpedido)

                    MenuDardeAlta()
                    opc = input()

                elif opc == "2":
                    cursor.execute("ROLLBACK TO SAVEPOINT uno")
                    print(mensaje_rol1)

                    MenuDardeAlta()
                    opc = input()

                elif opc == "3":    
                    cursor.execute("ROLLBACK TO SAVEPOINT cero")
                    print(mensaje_rol0)
                    break

                else:
                    print(mensaje_error)

            if opc == '4':
                cursor.execute("COMMIT")
                os.system('clear')
                print(mensaje_exito)

            MostrarIndice()
            ans = input()
        else:
            print(mensaje_error)
            MostrarIndice()
            ans = input()

    CerrarConexion(conexion)

except Exception as err:
    print("Error: ", err)
