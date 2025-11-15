import sys
sys.path.insert(0, "./libs")  

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []

def read_csv_file(filepath):
    data = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return data


@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    print("hello")
    product_id = request.args.get('id')
    error = None
    products_list = []

    if source not in ['json', 'csv']:
        error = "Wrong source"
        return render_template('product_display.html', products=[], error=error)

    if source == 'json':
        products_list = read_json_file('products.json')
    elif source == 'csv':
        products_list = read_csv_file('products.csv')

    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in products_list if p['id'] == product_id]
            if filtered:
                products_list = filtered
            else:
                error = "Product not found"
                products_list = []
        except ValueError:
            error = "Invalid id provided"
            products_list = []

    return render_template('product_display.html', products=products_list, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
