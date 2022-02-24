import psycopg2
import math
from tabulate import tabulate
def  post(x,y,p):
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
    cursor.execute("INSERT INTO Factorial(num,fac,div) VALUES (%s, %s, %s);", (x, y, p))
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
    cursor.execute("SELECT * from factorial;")
    print(tabulate(cursor, headers=["ID", "NUMERO", "FACTORIAL", "DIVISIBLE?"], tablefmt="fancy_grid", numalign ="center"))
print("Factorial de un numero\n")
r=0
while True:
    try:
        print("Elija una opcion:\n1.Correr el Programa\n2.Mostrar el Historial\n3.Salir")
        b=int(input("Elija:\n"))
        if b>3 or b<=0:
            print("Valor ingresado fuera del rango del menu.\n")
        elif b==1:
            while True:
                try:
                    a = int(input("Ingrese su numero: \n"))
                    if a<0:
                        print("A ingresado un numero negativo o no entero vuelva a intentarlo")
                    else:
                        if a%7 != 0:
                            f="NO"
                            print("El numero "+ f+ " Divisible entre 7, regresando al menu principal")
                            post(a,r,f)
                            file = open("C:/Users/Roberto/Documents/Proyectos/TAREA 1/factorial.txt","w")
                            file.write("El numero "+ f+ " Divisible entre 7, regresando al menu principal")
                            file.close()
                            break
                        elif a%7==0:
                            r= math.factorial(a)
                            f="SI"
                            print("El Factorial de "+str(a)+" es: "+str(r))
                            post(a,r,f)
                            file = open("C:/Users/Roberto/Documents/Proyectos/TAREA 1/factorial.txt","w")
                            file.write("El Factorial de "+str(a)+" es: "+str(r))
                            file.close()
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
        #print(repr(e))

exit(0)
