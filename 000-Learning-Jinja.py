from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader("templates-jinja")
env = Environment(loader=file_loader)


# Hello, World!
template = env.get_template("hello_world.txt")
output = template.render()
print(output)
print("\n")


# Variables
template = env.get_template("lamb.txt")
output = template.render(name="Mary")
print(output)

output = template.render(name="Jason")
print(output)
print("\n")


# Complex variables
person = {
    "name": "Bob",
    "animal": "dog"
}
template = env.get_template("animal.txt")
output = template.render(data=person)
print(output)
print("\n")


# Conditionals
template = env.get_template("truth.txt")
output = template.render(truth=True)
print(output)

output = template.render(truth=False)
print(output)
print("\n")


# For loops
rgb = ["red", "green", "blue"]
template = env.get_template("rainbow.txt")
output = template.render(colors=rgb)
print(output)
print("\n")


# Template Inheritance
template = env.get_template("base.html")
output = template.render(title="Page Title")
print(output)

template = env.get_template("child.html")
output = template.render(title="Page Title", body="My content")
print(output)