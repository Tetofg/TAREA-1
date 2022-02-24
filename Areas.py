import psycopg2
from tabulate import tabulate
import numpy as np
def  post(x,y,z,w):
    try:
        conexion = psycopg2.connect(
            host = "localhost",
            port = "5432",
            user = "postgres",
            password = "123fgthg",
            dbname = "HWP"
            )
    except:
        print("Sin Conexion Exitosa\n")
            
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO areas(fig, BaOR, h, A) VALUES (%s, %s, %s, %s);", (x, y, z, w))
    conexion.commit()
    cursor.close()
    conexion.close()

def ret():
    try:
        conexion = psycopg2.connect(
            host = "localhost",
            port = "5432",
            user = "postgres",
            password = "123fgthg",
            dbname = "HWP"
            )
    except:
        print("Sin Conexion Exitosa\n")
    
    cursor = conexion.cursor()
    cursor.execute("SELECT * from areas;")
    print(tabulate(cursor, headers=["ID", "FIGURA", "BASE O RADIO", "ALTURA", "AREA"], tablefmt="fancy_grid", numalign ="center"))

print("AREA DE DIFERENTES FIGURAS GEOMETRICAS \n")
while True:
    try:
        print("Elija una opcion:\n1.Correr el Programa\n2.Mostrar el Historial\n3.Salir")
        b=int(input("Elija:\n"))
        if b>3 or b<=0:
            print("Valor ingresado fuera del rango del menu.\n")
        elif b==1:
            while True:
                try:
                    print("A continuacion elija la figura a la cual necesitasacar el area\n")
                    print("Elija una opcion:\n1.Circulo\n2.Triangulo\n3.Cuadrado\n4.Rectangulo")
                    r=int(input("Elija:\n"))
                    h=0
                    if r>4 or b<=0:
                        print("Valor ingresado fuera del rango del menu.\n")
                    if r==1:
                        ra=int(input("Ingrese el radio del Circulo:\n"))
                        fig="Circulo"
                        a=np.pi*pow(ra,2)
                    if r==2:
                        ra=int(input("Ingrese  la base del Triangulo:\n"))
                        h= int(input("Ingrese la altura del triangulo:\n"))
                        fig="Triangulo"
                        a=ra*h*1/2
                    if r==3:
                        ra=int(input("Ingrese  el lado del cuadrado:\n"))
                        h = ra
                        a= pow(ra,2)
                        fig="Cuadrado"
                    if r==4:
                        ra = int(input("Ingrese la base del rectangulo\n"))
                        h = int(input("Ingrese la altura del rectangulo\n"))
                        a=ra*h
                        fig="Rectangulo"
                    print("El Area del "+ fig+" es:"+str(a)+" \n")
                    post(fig, ra, h, a)
                    break 
                except Exception as e:
                    print("\n A ingresado un valor o Caracter no valido por favor, ingrese una opcion correcta:\n")
                    print(repr(e))
        elif b==2:
            ret()
        elif b==3:
            break

    except Exception as e:
        print("\n A ingresado un valor o Caracter no valido por favor, ingrese una opcion correcta:\n")
        print(repr(e))

exit(0)