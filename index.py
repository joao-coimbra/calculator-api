from sanic import Sanic, response
from api import api

app = Sanic(__name__)
app.blueprint(api)


@app.route("/")
def display(request):
    return response.file('views/index.html')


@app.route("/download/<filename:str>")
def display(request, filename: str):
    return response.file(filename)


if __name__ == "__main__":
    app.run(
        debug=True
    )
