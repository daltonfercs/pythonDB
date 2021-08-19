import mysql.connector

mydb = mysql.connector.connect(
    host    =   'localhost',
    user    =   'dalstrom',
    password =  'dfcs',
    database  = 'prueba'     

)
cursor  =   mydb.cursor()

#listar db
#cursor.execute('select * from Usuario')
#resultado = cursor.fetchall()

#ver definiciones de datos
#cursor.execute('show create table Usuario')
#resultado = cursor.fetchall()

#Insertar datos
sql =   'insert into Usuario(nombre, email) values(%s, %s)'
values =    ('dalstrom', 'dalstrom@dfcs.dc')

cursor.execute(sql, values)
mydb.commit()


#print(resultado)
print(cursor.rowcount)