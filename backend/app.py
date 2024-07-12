# from flask import Flask, jsonify, send_from_directory
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route('/products', methods=['GET'])
# def get_products():
#     products = [
#         {'id': 1, 'image': 'apples-101-about-1440x810.jpg' 'name': 'Fresh Onion', 'description': '1kg', 'price': '₹31', 'discount': '25%' }
       
#         # Add more products as needed
#     ]
#     return jsonify({'products': products})

# @app.route('./images/<path:filename')
# def serve_image(filename):
#     return send_from_directory(os.path.join(app.root_path, 'static/images'), filename)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/products', methods=['GET'])
def get_products():
    products = [
        {'id': 1, 'image': 'apples-101-about-1440x810.jpg', 'name': 'Fresh Onion', 'description': '1kg', 'price': '₹31', 'discount': '25%'},
        {'id': 2, 'image': 'apples-101-about-1440x810.jpg', 'name': 'Fresh Orange', 'description': '1kg', 'price': '₹50', 'discount': '20%'},
        {'id': 3, 'image': 'apples-101-about-1440x810.jpg', 'name': 'Fresh Onion', 'description': '1kg', 'price': '₹31', 'discount': '25%'},
        {'id': 4, 'image': 'apples-101-about-1440x810.jpg', 'name': 'Fresh Orange', 'description': '1kg', 'price': '₹50', 'discount': '20%'},
        {'id': 5, 'image': 'apples-101-about-1440x810.jpg', 'name': 'Fresh Onion', 'description': '1kg', 'price': '₹31', 'discount': '25%'},
        {'id': 6, 'image': 'apples-101-about-1440x810.jpg', 'name': 'Fresh Onion', 'description': '1kg', 'price': '₹31', 'discount': '25%'},
        {'id': 7, 'image': 'apples-101-about-1440x810.jpg', 'name': 'Fresh Onion', 'description': '1kg', 'price': '₹31', 'discount': '25%'},
        {'id': 8, 'image': 'apples-101-about-1440x810.jpg', 'name': 'Fresh Orange', 'description': '1kg', 'price': '₹50', 'discount': '20%'}
    ]
    return jsonify({'products': products})

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(os.path.join(app.root_path, 'static/images'), filename)

if __name__ == '__main__':
    app.run(debug=True)
