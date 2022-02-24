import psycopg2
from tabulate import tabulate

def  post(x,y,z):
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
    cursor.execute("INSERT INTO TAXI(modelo, km, status) VALUES (%s, %s, %s);", (x, y, z))
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
    cursor.execute("SELECT * from Taxi;")
    print(tabulate(cursor, headers=["MODELO", "KILOMETRAJE", "STATUS"], tablefmt="fancy_grid", numalign ="center"))


print("PROMEDIO DE NOTAS \n")
while True:
    try:
        print("Elija una opcion:\n1.Correr el Programa\n2.Mostrar el Historial\n3.Salir")
        b=int(input("Elija:\n"))
        if b>3 or b<=0:
            print("Valor ingresado fuera del rango del menu.\n")
        elif b==1:
            status=""
            model=int(input("Ingrese el modelo del taxi: "))
            km=int(input("Ingrese el recorrido en Km del taxi: "))
            if model<2007 and 20<km:
                print("Debe renovarse")
                status="Debe renovarse"
            
            elif 2007<=model<=2013 and 20000==km:
                print("Debe recibir mantenimiento")
                status="Debe recibir mantenimiento"

            elif model>2013 and 10000>km:
                print("Esta en optimas condiciones")
                status="Esta en optimas condiciones"
            else:
                print("Mecánico")
                status="Mecánico"
            post(model, km, status)
        elif b==2:
            ret()
        elif b==3:
            break

    except Exception as e:
        print("\n A ingresado un valor o Caracter no valido por favor, ingrese una opcion correcta:\n")
        print(repr(e))

exit(0)