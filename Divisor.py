import psycopg2
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
    cursor.execute("INSERT INTO Divisores(numero,divisores) VALUES (%s, %s  );", (x, y))
    conexion.commit()
    cursor.close()
    conexion.close()

print("Divisores de un numero\n")
print("A continuacion ingrese su numero:\n")
a = int(input("Ingrese su numero \n"))
r=[]
z=1
for z in range(1,a+1):
    b = a%z
    if b == 0:
        r.append(z)

print("Los Divisores de "+str(a)+" son: "+str(r))
post(a,r)
file = open("C:/Users/Roberto/Documents/Proyectos/TAREA 1/Divisor.txt","w")
file.write("Los Divisores de "+str(a)+" son: "+str(r))
file.close()
exit(0)