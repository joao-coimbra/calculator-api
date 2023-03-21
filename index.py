from sanic import Sanic, response
from api import api

app = Sanic(__name__)
app.blueprint(api)


@app.route("/")
def display(request):
    return response.file('views/index.html')


@app.route("/download/<filename:str>")
def download(request, filename: str):
    print(filename)
    try:
        return response.file('static/'+filename)
    except Exception:
        return response.json({'message': 'Could not download'})


if __name__ == "__main__":
    app.run(
        debug=True
    )
