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
    cursor.execute("INSERT INTO maxmin(nummax,nummin,resultado) VALUES (%s, %s, %s);", (x, y,z))
    conexion.commit()
    cursor.close()
    conexion.close()
print("Numeros de mayor a menor\n")
r=[]
while True:
    try:
        n1=int(input("Ingrese el primer numero:\n "))
        n2=int(input("Ingrese el segundo numero:\n"))
        if n1>n2:
            for x in range(n1,n2-1,-1):
                r.append(x)
            print("Los numeros de mayor a menor son:\n",str(r))
            post(n1,n2,r)
            file = open("C:/Users/Roberto/Documents/Proyectos/TAREA 1/MayorAMenor.txt","w")
            file.write("Los numeros de mayor a menor son:\n"+str(r))
            file.close()
            break
        if n1<n2:
            for x in range(n2,n1-1,-1):
                r.append(x)
            print("Los numeros de mayor a menor son:\n",str(r))
            post(n2,n1,r)
            file = open("C:/Users/Roberto/Documents/Proyectos/TAREA 1/MayorAMenor.txt","w")
            file.write("Los numeros de mayor a menor son:\n"+str(r))
            file.close()
            break
    except Exception as e:
        print("\n A ingresado un valor o Caracter no valido por favor, ingrese una opcion correcta:\n")
        print(repr(e))

exit(0)
