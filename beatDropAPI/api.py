import falcon.asgi

api = falcon.asgi.App(cors_enable=True)


class Server:
    async def on_get(self, req, res):
        responseText = "Hello World!"
        res.media = {"response": f"The Server says:{responseText}"}


api.add_route("/v1/server", Server())
