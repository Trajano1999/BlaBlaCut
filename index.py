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

import pyodbc
import os                                                                                          # para limpiar la consola

# -------------------------------------------------------------------------------------------------
# MENÚS
# -------------------------------------------------------------------------------------------------

def MenuBienvenida():
    print()
    print(" ______  _         ______  _          _____         _   ")
    print(" | ___ \| |        | ___ \| |        /  __ \       | |  ")
    print(" | /_/ /| |  __ _  | |_/ /| |  __ _ |  /  \/ _   _ | |_ ")
    print(" | ___ \| | / _` | | ___ \| | / _` || |     | | | || __|")
    print(" | |_/ /| || (_| | | |_/ /| || (_| ||  \__/|| |_| || |_ ")
    print(" \____/ |_| \__,_| \____/ |_| \__,_| \____/ \__,__| \__|")    
    print()
    print("1.- Iniciar sesión")
    print("2.- Crear cuenta como Cliente")
    print("3.- Crear cuenta como Peluquero")
    print("4.- Acceder sin identificarse")                                                         # jjj
    print()

def MenuPrincipal():
    print()
    print("1.- Mi perfil")
    print("2.- Ver listado de Peluqueros")
    print("3.- Añadir una Cita")
    print("4.- Mensajes")
    print("5.- Añadir valoración")
    print("6.- Reportar incidencia")
    print("7.- Cerrar Sesión")
    print()

def MenuPerfil():
    print()
    print("1.- Ver       Perfil")
    print("2.- Modificar Perfil")
    print("3.- Eliminar  Perfil")                                                                  # solo si es peluquero
    print("4.- Volver atrás")
    print()

def MenuMensajes():
    print()
    print("1.- Escribir un mensaje")
    print("2.- Eliminar un mensaje")
    print("3.- Volver atrás")
    print()

def MenuCitas():
    print()
    print("1.- Ver citas")
    print("2.- Crear     una cita")                                                                # realizar el pago tras crear una cita
    print("3.- Eliminar  una cita")
    print("4.- Modificar una cita")
    print("5.- Volver atrás")
    print()

def MenuValoraciones():
    print()
    print("1.- Añadir valoración")
    print("2.- Añadir comentario")
    print("3.- Añadir fotorafía")
    print()

try: 
# jjj
#    conexion = pyodbc.connect('                                                                   \
#        DRIVER={Devart ODBC Driver for Oracle};                                                   \
#        Direct       = True;                                                                      \
#        Host         = oracle0.ugr.es;                                                            \
#        Service Name = practbd.oracle0.ugr.es;                                                    \
#        User ID      = x7555876;                                                                  \
#        Password     = x7555876')
    
    MenuBienvenida()

except Exception as err:
    print("Error: ", err)
