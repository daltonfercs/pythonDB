import mysql.connector

mydb = mysql.connector.connect(
    host    =   'localhost',
    user    =   'dalstrom',
    password =  'dfcs',
    database  = 'prueba'     

)
cursor  =   mydb.cursor()

cursor.execute('select * from Usuario')
resultado = cursor.fetchall()

print(resultado)