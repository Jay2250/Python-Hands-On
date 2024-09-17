from flask import Flask,render_template,request,redirect,url_for

#initialize flask app
appLogin = Flask(__name__)
print(appLogin)

#create routes for the login page
@appLogin.route('/')
def login():
    return render_template('login.html')

#Create a route to handle the login form submission
@appLogin.route('/login',methods =['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']
    
    #Simple username and password authentication
    if username == 'admin' and password == 'password':
        # return f'Welcome {username}'
        return redirect(url_for("show_dashboard"))
    else:
        return "Invalid username or password, Please Try again"

@appLogin.route('/dashboard')
def show_dashboard():
    return render_template('dashboard.html')

#run the flask app
if __name__ == '__main__':
    appLogin.run(debug=True)