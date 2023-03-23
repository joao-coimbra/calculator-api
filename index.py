from sanic import Sanic, response
from api import api

app = Sanic(__name__)
app.blueprint(api)

app.static("/", "views/index.html")

# string -> str, Vercel doesn't support Sanic 21.12, only up to 19.6
# C:\Python310\lib\site-packages\sanic_routing\route.py:355: DeprecationWarning: Use of 'string' as a path parameter type is deprected, and will be removed in Sanic v21.12. Instead, use <filename:str>.
@app.route("/download/<filename>")
def ador(request, filename: str):
    return response.file('static/'+filename)


if __name__ == "__main__":
    app.run(
        debug=True
    )
