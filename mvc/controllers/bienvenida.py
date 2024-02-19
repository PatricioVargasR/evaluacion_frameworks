import web

render = web.template.render('mvc/views/')

class Bienvenida:

    def GET(self):
        try:
            return render.bienvenida()
        except Exception as error:
            return f'Ocurrió un error {error}'
