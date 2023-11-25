from conex import conn
import traceback


class RecepcionistaDAO():
    
    #Constructor
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "@X73y18z64", "vete2")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    def validarLogin(self, recep):
        sql = "select RUNRECEPCION from RECEPCIONISTA where RUNRECEPCION = %s and CLAVE = %s"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (recep.getRun(), recep.getClave(),))
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado