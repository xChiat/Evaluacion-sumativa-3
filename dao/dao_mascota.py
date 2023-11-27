from conex import conn
import traceback

class MascotaDAO():

    #Constructor
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "@X73y18z64", "vete2")
        except Exception as ex:
            print(ex)
    
    #Conexion a la BD
    def getConex(self):
        return self.conn
    
    #Trae tabla mascota completa
    def prepareMascota(self):
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute("select IDMASCOTA, IDTIPO,  NOMBREMASCOTA, EDADMASCOTA from MASCOTAS")
            result = cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return result
    
    
    #Agrega objeto a Cargo
    def addMascota(self,mascota):
        cliente = "select IDCLIENTE from CLIENTE WHERE RUNCLIENTE = %s"
        sql = "insert into MASCOTAS (IDMASCOTA, NOMBREMASCOTA, EDADMASCOTA, IDTIPO, IDCLIENTE) values (%s,%s,%s,%s,%s)"
        c = self.getConex()
        cur = c.getConex().cursor()
        cur.execute(cliente,(mascota.getCliente(),))
        result = cur.fetchone()
        mensaje = ""
        if result is not None:
            cliente_id = result[0]  # Ajusta esto según la estructura real de tu resultado
            tipo_id = 1 if mascota.getTipoMascota().lower() == "perro" else 2
            # Resto del código...
        else:
            mensaje = "No se encontró el cliente en la base de datos."
        
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (mascota.getIdMascota(),mascota.getNombMascota(),mascota.getEdad(),tipo_id,cliente_id))
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
    
    #Elimina objeto de Mascota
    def delMascota(self, mascota):
        sql = "delete from MASCOTAS where IDMASCOTA = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (mascota.getIdMascota(),))
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
    
    #Modifica Objeto de Mascota
    def updateMascota(self, mascota):
        sql = "update MASCOTAS set NOMBREMASCOTA = %s, IDTIPO = %s, EDADMASCOTA = %s where IDMASCOTA = %s"
        c = self.getConex()
        tipo_id = 1 if mascota.getTipoMascota().lower() == "perro" else 2
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (mascota.getNombMascota(),tipo_id,mascota.getEdad(),mascota.getIdMascota(),))
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

  
