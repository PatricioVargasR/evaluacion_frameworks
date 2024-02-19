import web
from ..models.modelo_sesion import ModeloSesion

render = web.template.render('mvc/views/')

class InicioSesion:

    def GET(self):
        try:
            username, password = '', ''
            return render.index(username, password)
        except Exception as error:
            return f'Ocurrió un error {error}'

    def POST(self):
        try:
            form = web.input()
            sesion = ModeloSesion()
            resultado = sesion.Inicio(form.username, form.password)
            if(not resultado):
                return render.index(username='', password='')
            else:
                raise web.seeother('/bienvenida')
        except Exception as error:
            return f'Ocurrió un error {error}'