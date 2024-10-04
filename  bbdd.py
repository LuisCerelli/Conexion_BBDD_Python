#descargar la bbdd de https://mariadv.org/download/ y las credenciales suelen ser (mysql -u root)

#pip install mysq-conector-python

import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user= 'root',
    password='xxxxxxxx',
    datebase= 'bbdd_prueba'
)

cursor = conexion.cursor()

nuevo_usuario = ('Juan', 30)

consulta = 'INSERT INTO usuarios(nombre, edad) VALUES (%S,%S)'

cursor.execute(consulta, nuevo_usuario)

conexion.commit()

print('Registro guardado')

conexion.close()

