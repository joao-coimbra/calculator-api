from sanic import Sanic, response
from api import api

app = Sanic(__name__)
app.blueprint(api)


@app.route("/")
def display(request):
    return response.file('views/index.html')


# string -> str, Sanic in Vercel dont support str, str in Sanic ^21
@app.route("/download/<filename:string>")
def ador(request, filename: str):
    try:
        return response.file('static/'+filename)
    except Exception:
        return response.text('The file could not be found', status=404)


if __name__ == "__main__":
    app.run(
        debug=True
    )
