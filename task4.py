# api.py
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# In-memory "database" (a list of dictionaries)
# We start with some sample data.
users = [
    {"id": 1, "name": "Arul", "email": "arul@example.com"},
    {"id": 2, "name": "Chandru", "email": "chandru@example.com"}
]
next_user_id = 3

# --- API Endpoints ---

# Endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Endpoint to get a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    global next_user_id
    if not request.json or 'name' not in request.json or 'email' not in request.json:
        return jsonify({"error": "Missing name or email in request body"}), 400
    
    new_user = {
        'id': next_user_id,
        'name': request.json['name'],
        'email': request.json['email']
    }
    users.append(new_user)
    next_user_id += 1
    return jsonify(new_user), 201

# Endpoint to update a user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    if not request.json:
        return jsonify({"error": "Invalid request"}), 400

    user['name'] = request.json.get('name', user['name'])
    user['email'] = request.json.get('email', user['email'])
    return jsonify(user)

# Endpoint to delete a user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user_to_delete = next((user for user in users if user['id'] == user_id), None)
    if not user_to_delete:
        return jsonify({"error": "User not found"}), 404
    
    users = [user for user in users if user['id'] != user_id]
    return jsonify({"message": f"User with id {user_id} has been deleted."})

# This runs the app
if __name__ == '__main__':
    # debug=True allows the server to auto-reload when you save changes
    app.run(debug=True)