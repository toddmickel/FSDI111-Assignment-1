from app import app    # From our app package (folder) import the app variable

@app.route("/")     # A decorator that maps paths to view functions
def hello():        # View function
    return "<h1>Hello World!</h1>"


@app.route("/about")
def about():
    me = {
        "first_name": "Todd",
        "last_name": "Mickel",
        "hobby": "Playing baseball with my son",
        "ok": True
    }
    return me