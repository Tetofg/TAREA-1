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
    cursor.execute("INSERT INTO NumVocG(Palabra, NumVoc) VALUES (%s, %s  );", (x, y))
    conexion.commit()
    cursor.close()
    conexion.close()


p = input("Ingrese una palabra: ")
p = p.lower()
v= ["a","e","i","o","u"]
veces=0
for x in range(len(p)):
    a=p[x]
    if a == v[0]:
        veces=veces+1
    elif a == v[1]:
        veces=veces+1
    elif a == v[2]:
        veces=veces+1
    elif a == v[3]:
        veces=veces+1
    elif a == v[4]:
        veces=veces+1

print("Aparecen %d las vocales en la palabra %s"%(veces,p))
file = open("C:/Users/Roberto/Documents/Proyectos/TAREA 1/CantVoc.txt","w")
file.write("Aparecen "+str(veces)+" vocales en la palabra "+p)
file.close()

post(p,veces)





exit(0)
