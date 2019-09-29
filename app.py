from flask import Flask

app = Flask(__name__)
FLASK_APP = app  # specifying flask app


@app.route('/')
def index():
    """Return welcome message."""
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
