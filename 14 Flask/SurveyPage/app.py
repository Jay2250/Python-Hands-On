from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homePage.html')

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        feedback = request.form['comments']
        gender = request.form['gender']
        age = request.form['age']
        return redirect(url_for('results', name=name, email=email, feedback=feedback,gender=gender, age=age))
    return render_template('surveyForm.html')

@app.route('/results')
def results():
    name = request.args.get('name')
    email = request.args.get('email')
    feedback = request.args.get('feedback')
    gender = request.args.get('gender')
    age = request.args.get('age')
    return render_template('result.html', name=name, email=email, feedback=feedback, gender=gender , age=age)

if __name__ == '__main__':
    app.run(debug=True)
