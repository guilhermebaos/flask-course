# 0. Resources
Course notes and code [here](https://github.com/jimdevops19/FlaskSeries).

# 1. Lauching a Flask App
We can launch a Flask app by simply doing the following:
1. Create a new directory
2. Run `pip install flask`
3. Create a python file `myapp.py` with some flask code
4. On the command line execute `set FLASK_APP=myapp.py` followed by `flask run`
5. Open the app!

## Debug Mode
If we are making many changes to the app, we can activate debug mode on by setting another enviornment variable. We only need to do `set FLASK_DEBUG=1` to turn on debug mode.

This mode refreshes the content of our app everytime we make a change in the source file.


# 2. Styling and Templates
We can create template pages by creating a `template` directory and storing our HTML files in there.

## Sending Data to Templates using Jinja
We can send data to our templates by passing additional optional arguments to the `render_template` function.

This can then be accessed in our template using the Jinja templating engine [Jinja Website](https://jinja.palletsprojects.com/en/3.1.x/). Also read [this primer](https://realpython.com/primer-on-jinja-templating/) on how to use Jinja!

We can also use this method to pass variables from Python to Javascript, as described in [this article](https://thewebdev.info/2022/04/03/how-to-pass-variables-from-python-flask-to-javascript/).