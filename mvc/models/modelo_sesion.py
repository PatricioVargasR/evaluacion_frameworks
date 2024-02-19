

class ModeloSesion:

    def Inicio(self, username:str, password:str):
        try:
            if username == 'usuario' and password == '1234':
                return True
        except Exception as error:
            return f'Ocurrió un error {error}'