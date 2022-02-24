import psycopg2
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
    cursor.execute("INSERT INTO ac3(n1, n2, n3, res) VALUES (%s, %s, %s, %s);", (x, y, z, w))
    conexion.commit()
    cursor.close()
    conexion.close()
print("A continuacion ingrese 3 numeros")
n1 = int(input("Primer Numero \n"))
n2 = int(input("Segundo Numero \n"))
n3 = int(input("Tercer Numero \n"))
a = ""
if n1>n2 and n2>n3:
    print("El Primer numero es el mas grande\n")
    t = n1+n2+n3
    a = str(t)
    print(a)
elif n2>n1 and n2>n3:
    print("El Segundo numero es el mas grande\n")
    t = n1*n2*n3
    a = str(t)
    print(a)
elif n3>n1 and n3>n2:
    print("El Tercer numero es el mas grande\n")
    a = str(n1)+str(n2)+str(n3)
    print(a)
elif n1==n2==n3:
    print("Todos son iguales:"+ str(n1)+", "+str(n2)+", "+str(n3))
    a="TODOS SON IGUALES"

post(n1,n2,n3,a)