from conex import conn
import traceback

class ClienteDAO():
    #Constructor
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "@X73y18z64", "vete2")
        except Exception as ex:
            print(ex)
    
    #Conexion a la BD
    def getConex(self):
        return self.conn
    
    #Trae tabla Cliente completa
    def prepareCliente(self):
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute("select RUNCLIENTE, NOMBRECLIENTE, APELLIDOCLIENTE, TELEFONOCLIENTE, CORREOCLIENTE from CLIENTE")
            result = cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return result
    
    
    #Agrega objeto a Cliente
    def agregarCliente(self,cliente):
        sql = "insert into CLIENTE (RUNCLIENTE, NOMBRECLIENTE, APELLIDOCLIENTE, TELEFONOCLIENTE, CORREOCLIENTE) values (%s,%s,%s,%s,%s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cliente.getRun(),cliente.getNombre(),cliente.getApellido(),cliente.getTelefono(),cliente.getCorreo(),))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos agregados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje
    
    #Elimina objeto de Cliente
    def eliminarCliente(self, cliente):
        c = self.getConex()
        cli= "select IDCLIENTE from CLIENTE WHERE RUNCLIENTE = %s"
        cur = c.getConex().cursor()
        cur.execute(cli,(cliente.getRun(),))
        result = cur.fetchone()
        if result is not None:
            cliente_id = result[0]
        else:
            mensaje = "No se encontró el cliente en la base de datos."
        try:
            msc = "delete from MASCOTAS where IDCLIENTE = %s"
            cur.execute(msc, (cliente_id,))
            c.getConex().commit()
            filas = cur.rowcount
            if filas > 0:
                mensaje ="Datos de las mascotas eliminados satisfactoriamente"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        sql = "delete from CLIENTE where RUNCLIENTE = %s"
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cliente.getRun(),))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos eliminados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje
    
    #Modifica Objeto de Cliente
    def modificarCliente(self, cliente):
        sql = "update CLIENTE set NOMBRECLIENTE = %s, APELLIDOCLIENTE = %s, CORREOCLIENTE = %s, TELEFONOCLIENTE = %s where RUNCLIENTE = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cliente.getNombre(),cliente.getApellido(),cliente.getCorreo(),cliente.getTelefono(),cliente.getRun(),))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos modificados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje
