from flask import Flask, request, render_template, redirect, url_for, flash
import inventory_manager  # Your existing code refactored into functions

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view_inventory')
def view_inventory():
    inventory = inventory_manager.load_inventory()
    return render_template('inventory.html', inventory=inventory)

@app.route('/add_product', methods=['POST'])
def add_product():
    product_id = request.form['product_id']
    product_name = request.form['product_name']
    category = request.form['category']
    price = request.form['price']
    stock = request.form['stock']

    result = inventory_manager.add_product_web(product_id, product_name, category, price, stock)
    flash(result)
    return redirect(url_for('index'))

if __name__ == '__main__':
    inventory_manager.initialize_csv()
    app.run(host='0.0.0.0', port=5000)
