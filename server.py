from sanic import Sanic, response
from api import api

app = Sanic(__name__)
app.blueprint(api)

@app.get('/about')
async def about(request):
    return response.json({
        "name": "Calculator API whit Sanic framework",
        "version": "1.0",
        "authors": ["João Henrique", "Thiago", "Felipe"],
        "private": True,
        "scripts": {
            "start": "sanic server.app",
        },
        "dependencies": {
            "python": "^3.10.4",
            "sanic": "22.9"
        }
    })

if __name__ == "__main__":
    app.run()
