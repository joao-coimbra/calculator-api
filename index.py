from sanic import Sanic, response
from api import api

app = Sanic(__name__)
app.blueprint(api)


@app.route("/")
def display(request):
    return response.file('views/index.html')


@app.route("/download")
async def download(request):
    return response.json({'message': 'Could not download'})

@app.route("/download/<filename:string>")
def ador(request, filename: str):
    return response.file('static/'+filename)


if __name__ == "__main__":
    app.run(
        debug=True
    )
