import falcon.asgi
import FileRoutes
api = falcon.asgi.App(cors_enable=True)
FileRoutes.Initialize(api)