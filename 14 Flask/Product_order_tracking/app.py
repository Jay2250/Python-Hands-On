from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        product = request.form['product'] 
        quantity = request.form['quantity']
        session['product'] = product
        session['quantity'] = quantity
        return redirect(url_for('shipping')) 
    return render_template('home.html')

@app.route('/shipping', methods=['GET','POST'])
def shipping():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        session['name'] = name
        session['address'] = address
        return redirect(url_for('orderSummary'))
    return render_template('shipping.html')

@app.route('/orderSummary', methods=['GET'])
def orderSummary():
    product = session.get('product')
    quantity = session.get('quantity')
    name = session.get('name')
    address = session.get('address')
    return render_template('orderSummary.html', product=product, quantity=quantity, name=name, address=address)

if __name__ == '__main__':
    app.run(debug=True)