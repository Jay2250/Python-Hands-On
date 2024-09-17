from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homePage.html')

@app.route('/check_age', methods=['POST'])
def check_age():
    username = request.form['username']
    age = int(request.form['age'])
    
    if age >= 18:
        return render_template('resultPage.html', age=age)
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
