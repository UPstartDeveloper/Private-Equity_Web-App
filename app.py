from flask import Flask, render_template

app = Flask(__name__)
FLASK_APP = app  # specifying flask app


@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html', msg="Welcome to Homely Properties")


if __name__ == '__main__':
    app.run(debug=True)
