from flask import Flask

# Name of the Python file
app = Flask(__name__)
print(app)


# This decorator specifies the part of the link after the domain
# As such, it says the route on the server we must take to arrive at this function
# In this case, it returns the page www.domain.com/
@app.route("/")
def hello_world():
    return "<h1>Hello World, again!</h1>"


# This function returns the page for www.domain.com/about
@app.route("/about")
def about_page():
    return "<h1>About Page</h1>"


# This function returns the page for www.domain.com/user/name_of_the_user
# This is called a dynamic route
@app.route("/user/<username>")
def user_page(username):
    return f"<h1>This is the about page of {username}</h1>"

