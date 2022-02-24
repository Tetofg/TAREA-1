import psycopg2
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
    cursor.execute("INSERT INTO plus2(numstr, numend, num2num) VALUES (%s, %s, %s);", (x, y,z))
    conexion.commit()
    cursor.close()
    conexion.close()
print("Numeros de dos en dos\n")
st=int(input("Ingrese el numero de inicio:\n"))
en=int(input("Ingrese el numero de fin:\n"))
r=[]
for x in range(st,en+1,2):
    r.append(x)

print("Los numeros son:", str(r))
post(st, en, r)
exit(0)