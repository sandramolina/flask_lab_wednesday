
from flask import render_template
from app import app
from models.orders_list import *

@app.route('/')
def index():
    return render_template("index.html", title="Shop X", order_list=order_list)

@app.route('/orders/<index>')
def order_by_index(index):
    int_index = int(index)
    return render_template("order.html", order=order_list[int_index])