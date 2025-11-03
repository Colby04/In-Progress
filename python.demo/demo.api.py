"""A simple REST-style API built with Flask. Demonstrates backend fundamentals — routing, JSON responses, and basic data handling. Author: Colby Rhodes."""

from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

items = [
    {"id": 1, "name": "Coconuts", "price": 2.99},
    {"id": 2, "name": "Pink Lady Apples", "price": 3.49},
]

@app.route("/")
def home():
        template = """
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Demo API Items</title>
            <style>
                body{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin:0;padding:24px;background:#fafafa;color:#111}
                h1{margin:0 0 12px}
                .muted{color:#666}
                ul{list-style:none;padding:0;margin:16px 0 0}
                li{padding:10px 0;border-bottom:1px solid #eee;display:flex;gap:8px;align-items:baseline}
                .id{font-weight:600;color:#555}
                .name{font-weight:600}
                .price{color:#444}
                .endpoints{margin-top:16px}
                code{background:#f2f2f2;padding:2px 6px;border-radius:4px}
                a{color:#0066cc;text-decoration:none}
                a:hover{text-decoration:underline}
            </style>
        </head>
        <body>
            <h1>Items <span class="muted">({{ items|length }})</span></h1>
            {% if items %}
            <ul>
                {% for it in items %}
                    <li>
                        <span class="id">#{{ it["id"] }}</span>
                        <span class="name">{{ it["name"] }}</span>
                        <span class="price">${{ '%.2f'|format(it["price"]) }}</span>
                    </li>
                {% endfor %}
            </ul>
            {% else %}
                <p class="muted">No items yet.</p>
            {% endif %}

            <div class="endpoints muted">
                API endpoints: <a href="/items">/items</a> (GET),
                <code>POST /items</code> with JSON <code>{"name":"","price":0}</code>
            </div>
        </body>
        </html>
        """
        return render_template_string(template, items=items), 200


@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items), 200


@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return jsonify(item), 200
    return jsonify(error="Item not found"), 404


@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()
    if not data or "name" not in data or "price" not in data:
        return jsonify(error="Invalid input"), 400

    new_item = {
        "id": len(items) + 1,
        "name": data["name"],
        "price": data["price"]
    }
    items.append(new_item)
    return jsonify(new_item), 201


if __name__ == "__main__":
    app.run(debug=True)
