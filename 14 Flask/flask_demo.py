from flask import Flask,render_template,request,redirect,url_for
#initialize flask app
app = Flask(__name__)

@app.route('/') # This route will handle requests to the root url "/"
def homePage():
    return "Welcome to HomePage"

if __name__ == '__main__':
    app.run(debug=True) # Starts the development server