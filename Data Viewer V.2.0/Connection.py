import pymysql
from plyer import notification

class Connection:

    def __init__(self):
        self.cnn=pymysql.connect(host="localhost",user="root",passwd="1012462766",database="app_data")

    def __str__(self):
        Consulta_datos=self.consulta_dato()
        aux=""
        for row in Consulta_datos:
            aux=aux + str(row) + "\n"
        return aux

    def consulta_dato(self):
        cur=self.cnn.cursor()
        cur.execute("SELECT * FROM consumos")
        Consulta_datos=cur.fetchall()
        cur.close()
        notification.notify(
        title='Nueva Consulta',
        message='Conexion exitosa con base SQL',
        app_icon='',
        timeout = 20)
        return Consulta_datos

    def buscar_dato(self, Id):
        cur=self.cnn.cursor()
        SQL="SELECT * FROM consumos WHERE Id = {}".format(Id)
        cur.execute(SQL)
        Consulta_datos=cur.fetchall()
        cur.close
        return Consulta_datos

    def insertar_dato(self, Id, Identificacion, FechaTransaccion, ValorTransaccion, CantidadProductos,UES,Producto):
        cur=self.cnn.cursor()
        SQL='''INSERT INTO consumos(Id, FechaTransaccion, ValorTransaccion, CantidadProductos,UES,Producto)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(Id, Identificacion, FechaTransaccion, ValorTransaccion, CantidadProductos,UES,Producto)
        cur.execute(SQL)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def eliminar_dato(self, Id):
        cur=self.cnn.cursor()
        SQL='''DELETE FROM consumos WHERE Id={}'''.format(Id)
        cur.execute(SQL)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def modificar_dato(self, Id, Identificacion, FechaTransaccion, ValorTransaccion, CantidadProductos,UES,Producto):
        cur=self.cnn.cursor()
        SQL='''UPDATE consumos SET  Identificacion='{}', FechaTransaccion='{}', ValorTransaccion='{}', 
        CantidadProductos='{}' , UES='{}', Producto='{}' WHERE Id={}'''.format(Id, Identificacion, FechaTransaccion, ValorTransaccion, CantidadProductos,UES,Producto)
        cur.execute(SQL)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()
        return n


