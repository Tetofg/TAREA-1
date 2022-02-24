import psycopg2
def  post(x,y,z,w,u,v):
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
    cursor.execute("INSERT INTO vowc(palabra, numa, nume, numi, numo, numu) VALUES (%s, %s, %s, %s, %s, %s);", (x, y, z, w, u, v))
    conexion.commit()
    cursor.close()
    conexion.close()

print("Numero de Vocales Individuales en una palabra")
strt = str(input("Ingrese su palabra:"))

voc=['a','e','i','o','u']
cant=[0,0,0,0,0]

for x in range(0, len(strt)):
    if strt[x]== voc[0]:
        cant[0]=cant[0]+1
    if strt[x]== voc[1]:
        cant[1]=cant[1]+1
    if strt[x]== voc[2]:
        cant[2]=cant[2]+1
    if strt[x]== voc[3]:
        cant[3]=cant[3]+1
    if strt[x]== voc[4]:
        cant[4]=cant[4]+1
print('La # de la vocal a es de: \n', cant[0])
print('La # de la vocal e es de: \n', cant[1])
print('La # de la vocal i es de: \n', cant[2])
print('La # de la vocal o es de: \n', cant[3])
print('La # de la vocal u es de: \n', cant[4])
post(strt, cant[0], cant[1], cant[2], cant[3], cant[4])
exit(0)