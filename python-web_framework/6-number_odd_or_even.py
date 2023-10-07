"""flask script that starts a Flask web application:
"""

from flask import Flask, escape, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/", defaults={"text": "is_cool"}, strict_slashes=False)
@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C {}".format(escape(text).replace("_", " "))


@app.route("/python/", defaults={"text": "is_cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    return "Python {}".format(escape(text).replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template("number.html", n=n)
    else:
        return "Not a valid input"


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    if isinstance(n, int):
        parity = "even" if n % 2 == 0 else "odd"
        return render_template("odd_even.html", n=n, parity=parity)
    else:
        return "Not a valid input"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
