from app import app
from flask import render_template

from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', orders=orders)


@app.route('/orders/<cust_number_passed>')
def single_order(cust_number_passed):
    return render_template('order.html', order=orders[int(cust_number_passed)]) 
# @app.route('/<name>')
# def greeting(name):
#     return f"Good Morning {name}"