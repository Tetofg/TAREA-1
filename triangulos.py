import psycopg2
from tabulate import tabulate
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
    cursor.execute("INSERT INTO triangulo(n1, n2, n3, res) VALUES (%s, %s, %s, %s);", (x, y, z, w))
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
    cursor.execute("SELECT * from triangulo;")
    print(tabulate(cursor, headers=["ID", "LADO 1", "LADO 2", "LADO 3", "TIPO DE TRIANGULO"], tablefmt="fancy_grid", numalign ="center"))

print("TIPO DE TRANGULO \n")
r=[]
while True:
    try:
        print("Elija una opcion:\n1.Correr el Programa\n2.Mostrar el Historial\n3.Salir")
        b=int(input("Elija:\n"))
        if b>3 or b<=0:
            print("Valor ingresado fuera del rango del menu.\n")
        elif b==1:
            print("A continuacion ingrese 3 numeros")
            n1 = int(input("Primer Numero \n"))
            n2 = int(input("Segundo Numero \n"))
            n3 = int(input("Tercer Numero \n"))
            a = ""
            if (n1==n2 and n1!=n3) or (n1==n3 and n1!=n2)  or (n2==n3 and n2!=n1):
                print("Es un triangulo Isoseles\n")
                a = "ISOCELES"
            elif n2!=n1 and n2!=n3 and n1!=n3:
                print("Es un Triangulo Escaleno\n")
                a = "Escaleno"

            elif n1==n2==n3:
                print("Es un triangulo Equilatero")
                a="Equilatero"
            post(n1,n2,n3,a)

        elif b==2:
            ret()
        elif b==3:
            break

    except Exception as e:
        print("\n A ingresado un valor o Caracter no valido por favor, ingrese una opcion correcta:\n")
        print(repr(e))

exit(0)