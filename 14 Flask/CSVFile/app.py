from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    file = None
    if request.method == 'POST':
        file = pd.read_csv(request.form['file'])
    return render_template('home.html', file=file.describe())


if __name__ == '__main__':
    app.run(debug=True)
