from sanic import Sanic, response
from api import api

app = Sanic(__name__)
app.blueprint(api)


@app.route("/")
def display(request):
    return response.file('index.html')


if __name__ == "__main__":
    app.run(
        debug=True
    )
