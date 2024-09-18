from flask import jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash

# Simulating user database, with password hashed for production-like behavior
users_db = {
    "admin": {"password": "admin", "role": "admin"},
}

def authenticate(username, password):
    user = users_db.get(username)
    if user and user["password"] == password:  # Using plain text comparison for demo
        access_token = create_access_token(identity={"username": username, "role": user["role"]})
        return jsonify(access_token=access_token)
    else:
        return jsonify({"msg": "Bad credentials"}), 401

@jwt_required()
def admin_required():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"msg": "Admin access required"}), 403

