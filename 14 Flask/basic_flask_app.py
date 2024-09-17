from flask import Flask

app = Flask(__name__)


@app.route('/')  # this route will handle requests to root url "/"
def homePage():
    return "Welcome to home page!"


if __name__ == '__main__':
    app.run(debug=True)

