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
    cursor.execute("INSERT INTO impar1(imapres, cantidad) VALUES (%s, %s);", (x, y))
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
    cursor.execute("SELECT * from impar1;")
    print(tabulate(cursor, headers=["ID", "IMPARES", "CANTIDAD"], tablefmt="fancy_grid", numalign ="center"))

print("Numeros impares del 1 al 100 \n")
r=[]
while True:
    try:
        print("Elija una opcion:\n1.Correr el Programa\n2.Mostrar el Historial\n3.Salir")
        b=int(input("Elija:\n"))
        if b>3 or b<=0:
            print("Valor ingresado fuera del rango del menu.\n")
        elif b==1:
            for x in range(1,100,2):
                r.append(x)
            print("Los numero impares del 1 al 100 son: \n ",r)
            post(r,len(r))
            file = open("C:/Users/Roberto/Documents/Proyectos/TAREA 1/impares.txt","w")
            file.write("Los numero impares del 1 al 100 son: \n "+ str(r))
            file.close()
        elif b==2:
            ret()
        elif b==3:
            break

    except Exception as e:
        print("\n A ingresado un valor o Caracter no valido por favor, ingrese una opcion correcta:\n")
        print(repr(e))

exit(0)