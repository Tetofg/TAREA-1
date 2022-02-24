import psycopg2
from tabulate import tabulate
def  post(x,y):
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
    cursor.execute("INSERT INTO bisiesto(yer, bis) VALUES (%s, %s);", (x, y))
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
    cursor.execute("SELECT * from bisiesto;")
    print(tabulate(cursor, headers=["ID", "AÑO", "BIS"], tablefmt="fancy_grid", numalign ="center"))

print("AÑOS BISIESTOS \n")
r=[]
while True:
    try:
        print("Elija una opcion:\n1.Correr el Programa\n2.Mostrar el Historial\n3.Salir")
        b=int(input("Elija:\n"))
        if b>3 or b<=0:
            print("Valor ingresado fuera del rango del menu.\n")
        elif b==1:
            o=int(input("Ingrese el año \n"))
            re =""
            if o % 4 == 0:
                if o % 100 == 0:
                    if o % 400 == 0:
                        print('El año es bisiesto')
                        re="Bisiesto"
                    else:
                        print('El año no es bisiesto')
                        re="No Bisiesto"
                else:
                    print('El año es bisiesto.')
                    re="Bisiesto"
            else:
                print('El año no es bisiesto.')
                re="No Bisiesto"
            post(o,re)
        elif b==2:
            ret()
        elif b==3:
            break

    except Exception as e:
        print("\n A ingresado un valor o Caracter no valido por favor, ingrese una opcion correcta:\n")
        print(repr(e))

exit(0)