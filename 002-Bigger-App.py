from flask import Flask, render_template

app = Flask(__name__)
print(app)


# Returns a rendered template from a HTML file
@app.route("/")
def hello_world():
    return render_template("002-home.html")

