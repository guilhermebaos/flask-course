from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
print(app)


# Returns a rendered template from a HTML file
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template("market.html", items=items)


# Based on this video: https://www.youtube.com/watch?v=9MHYHgh4jYc
# State that this route can use "GET" and "POST" methods, the default is only GET
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST": 
        user = request.form["name"]
        return render_template("login.html", usr=user)
    else:
        return render_template("login.html", usr=False)


@app.route("/<usr>")
def user(usr):
    return f"<h1>Hello, {usr}!</h1>"


@app.route("/lists")
def lists():
    return render_template("lists.html")
