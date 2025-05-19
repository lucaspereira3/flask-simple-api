# Simple Flask API Example

from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample data (in-memory database)
items = [
    {"id": 1, "name": "Item 1", "description": "This is the first item"},
    {"id": 2, "name": "Item 2", "description": "This is the second item"}
]
next_id = 3

# --- API Endpoints ---

@app.route("/")
def home():
    """Home endpoint to check if the API is running."""
    return jsonify({"message": "Welcome to the Simple API!"})

@app.route("/items", methods=["GET"])
def get_items():
    """Endpoint to get all items."""
    return jsonify({"items": items})

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    """Endpoint to get a specific item by its ID."""
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify({"item": item})
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route("/items", methods=["POST"])
def add_item():
    """Endpoint to add a new item."""
    global next_id
    if not request.json or not "name" in request.json:
        return jsonify({"error": "Missing 'name' in request body"}), 400
    
    description = request.json.get("description", "") # Optional description
    
    new_item = {
        "id": next_id,
        "name": request.json["name"],
        "description": description
    }
    items.append(new_item)
    next_id += 1
    return jsonify({"message": "Item added successfully", "item": new_item}), 201

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    """Endpoint to update an existing item."""
    item = next((item for item in items if item["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
        
    if not request.json:
         return jsonify({"error": "Request body cannot be empty for update"}), 400

    # Update fields if provided in the request
    item["name"] = request.json.get("name", item["name"])
    item["description"] = request.json.get("description", item["description"])
    
    return jsonify({"message": "Item updated successfully", "item": item})

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    """Endpoint to delete an item."""
    global items
    initial_length = len(items)
    items = [item for item in items if item["id"] != item_id]
    if len(items) < initial_length:
        return jsonify({"message": "Item deleted successfully"})
    else:
        return jsonify({"error": "Item not found"}), 404

# --- Run the App ---

if __name__ == "__main__":
    # Runs the Flask development server
    # Debug=True allows for auto-reloading on code changes and provides detailed error pages
    # Host='0.0.0.0' makes the server accessible from other devices on the network
    print("Starting Flask API server...")
    print("Access it at http://127.0.0.1:5000 or http://<your-ip>:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
