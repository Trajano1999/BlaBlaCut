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
    print("-------------------------")
    print("|      BLA BLA CUT      |")
    print("-------------------------")
    print()
    print("1.- Iniciar sesión")
    print("2.- Crear cuenta como Cliente")
    print("3.- Crear cuenta como Peluquero")
    print("4.- Acceder sin identificarse")
    print()

def MenuIniciarSesion():
    print()
    print("1.- Iniciar sesión")
    print("2.- Crear cuenta como Cliente")
    print("3.- Crear cuenta como Peluquero")
    print("4.- Acceder sin identificarse")
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
