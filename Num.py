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
    cursor.execute("INSERT INTO numvocg(palabra, numvoc) VALUES (%s, %s);", (x, y))
    conexion.commit()
    cursor.close()
    conexion.close()
print("Numero de Vocales Totale en una palabra")
strt = str(input("Ingrese su palabra:"))

voc=['a','e','i','o','u']
cont=0

for x in range(0, len(strt)):
    if strt[x]== voc[0]:
        cont=cont+1
    if strt[x]== voc[1]:
        cont=cont+1
    if strt[x]== voc[2]:
        cont=cont+1
    if strt[x]== voc[3]:
        cont=cont+1
    if strt[x]== voc[4]:
        cont=cont+1
print('La palabra '+ strt + " tiene: " +str(cont))
post(strt, cont)
exit(0)