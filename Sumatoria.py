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
    cursor.execute("INSERT INTO sumatoria(nummax, resultado) VALUES (%s, %s);", (x, y))
    conexion.commit()
    cursor.close()
    conexion.close()


print("Ingrese el numero maximo:\n ")
num = int(input())
b=0
for i in range(1, num+1):
    b=b+i
print("La suma es: ", b)
post(num,b)
exit(0)