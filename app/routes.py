from flask import Blueprint, request, jsonify
from app import db
from app.models import Book
from app.auth import admin_required
import requests

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{"title": book.title, "author": book.author, "isbn": book.isbn} for book in books])

@main_bp.route('/books', methods=['POST'])
@admin_required
def create_book():
    data = request.json
    if Book.query.filter_by(isbn=data["isbn"]).first():
        return jsonify({"msg": "ISBN already exists"}), 400

    # Communicate with Node.js to upload cover image
    files = {"cover_image": request.files['cover_image']}
    upload_response = requests.post("http://localhost:3000/upload-cover", files=files)
    if upload_response.status_code != 200:
        return jsonify({"msg": "Error uploading cover image"}), 500

    new_book = Book(title=data['title'], author=data['author'], isbn=data['isbn'], cover_image=upload_response.json().get('path'))
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"msg": "Book created successfully"}), 201

