from sanic import Sanic, response
from api import api

app = Sanic(__name__)
app.blueprint(api)


@app.get('/')
@app.get('/about')
async def about(request):
    return response.json({
        "name": "Calculator API with Sanic framework",
        "version": "1.0",
        "private": True,
    })

if __name__ == "__main__":
    app.run()
