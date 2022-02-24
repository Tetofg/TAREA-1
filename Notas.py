import psycopg2
from tabulate import tabulate
def  post(x,y,z,w,u):
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
    cursor.execute("INSERT INTO notas(n1, n2, n3, mean, pass) VALUES (%s, %s, %s, %s, %s);", (x, y, z, w, u))
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
    cursor.execute("SELECT * from notas;")
    print(tabulate(cursor, headers=["NOTA 1", "NOTA 2", "NOTA 3", "PROMEDIO", "ESTATUS"], tablefmt="fancy_grid", numalign ="center"))

print("PROMEDIO DE NOTAS \n")
while True:
    try:
        print("Elija una opcion:\n1.Correr el Programa\n2.Mostrar el Historial\n3.Salir")
        b=int(input("Elija:\n"))
        if b>3 or b<=0:
            print("Valor ingresado fuera del rango del menu.\n")
        elif b==1:
            print("Ingrese la Primera nota:\n")
            n1=int(input("Nota 1:\n"))

            while n1<0:
                print("A ingresado un valor negativo, verifique\n")
                print("Ingrese la Primera nota:\n")
                n1=int(input("Nota 1:\n"))
            print("Ingrese la Segunda nota:\n")
            n2=int(input("Nota 2:\n"))

            while n2<0:
                print("A ingresado un valor negativo, verifique\n")
                print("Ingrese la Segunda nota:\n")
                n2=int(input("Nota 2:\n"))

            print("Ingrese la Tercera nota:\n")
            n3=int(input("Nota 3:\n"))
            while n3<0:
                print("A ingresado un valor negativo, verifique\n")
                print("Ingrese la Tercera nota:\n")
                n3=int(input("Nota 3:\n"))

            mean=(n1+n2+n3)/3
            if mean>=60:
               pas = "APROBADO"
            if mean<60:
                pas="REPROBADO"
            print("EL ESTADO ES "+pas+ " CON UN PROMEDIO DE: "+ str(mean))
            post(n1,n2,n3,mean,pas)
            
        elif b==2:
            ret()
        elif b==3:
            break

    except Exception as e:
        print("\n A ingresado un valor o Caracter no valido por favor, ingrese una opcion correcta:\n")
        print(repr(e))

exit(0)