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
        sql = "insert into MASCOTA (IDMASCOTA, IDTIPO, NOMBREMASCOTA, EDADMASCOTA) values (%s,%s,%s,%s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (mascota.getIdMascota(),mascota.getTipoMascota(),mascota.getNombreMascota(),mascota.getEdad(),))
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
        sql = "delete from MASCOTA where IDMASCOTA = %s"
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
        sql = "update MASCOTA set NOMBREMASCOTA = %s, IDTIPO = %s, EDADMASCOTA = %s where IDMASCOTA = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (mascota.getNombreMascota(),mascota.getTipoMascota(),mascota.getEdad(),mascota.get_rut(),))
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
    
    def findMascota(self, idmascota):
        sql = "SELECT NOMBREMASCOTA, IDTIPO, EDADMASCOTA FROM MASCOTA WHERE IDMASCOTA = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (idmascota,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except Exception as ex:
            print(traceback.print_exc())
            return None
        finally:
            if c.getConex().is_connected():
                c.closeConex()
    
  
