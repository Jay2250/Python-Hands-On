from flask import Flask,render_template,request,redirect,url_for,flash

app = Flask(__name__)
print(app)

@app.route('/')
def login():
    return render_template('homePage.html')
@app.route('/check_age', methods = ['POST'])
def check_age():
    username = request.form['username']
    age = int(request.form['age'])
    if age >= 18:
        return render_template('resultPage.html', age=age)
    else:
        flash("You are under age")
        return redirect(url_for('login'))
@app.route('/result')
def result():
     return render_template('resultPage.html')
 
if __name__ == '__main__':
    app.run(debug=True)

    
