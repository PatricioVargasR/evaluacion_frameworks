import web

urls = (
    "/", "mvc.controllers.inicio_sesion.InicioSesion",
    "/bienvenida", "mvc.controllers.bienvenida.Bienvenida"
)

app = web.application(urls, globals())


if __name__ == '__main__':
    app.run()