from flask import Blueprint, render_template, request, jsonify
from .tables import db, Product, Sale

main = Blueprint('main', __name__)

# ---------- Homepage ----------
@main.route('/')
def index():
    return "🏪 Store Management Dashboard is running!"


# ---------- Products ----------
@main.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    result = [
        {"id": p.id, "name": p.name, "quantity": p.quantity, "price": p.price}
        for p in products
    ]
    return jsonify(result)


@main.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    product = Product(
        name=data['name'],
        quantity=data.get('quantity', 0),
        price=data['price']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product added successfully!"}), 201


# ---------- Sales ----------
@main.route('/sales', methods=['POST'])
def record_sale():
    data = request.get_json()
    sale = Sale(
        product_id=data['product_id'],
        quantity_sold=data['quantity_sold'],
        date=data['date']
    )
    db.session.add(sale)
    db.session.commit()
    return jsonify({"message": "Sale recorded successfully!"}), 201


@main.route('/sales', methods=['GET'])
def get_sales():
    sales = Sale.query.all()
    result = [
        {"id": s.id, "product_id": s.product_id, "quantity_sold": s.quantity_sold, "date": s.date}
        for s in sales
    ]
    return jsonify(result)
