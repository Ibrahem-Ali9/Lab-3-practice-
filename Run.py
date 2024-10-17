from flask import Flask, request, jsonify
# Simple user story 
# As a bookowner i want you to manage my inventory through an api so i can perform operation such as (Delete, Update, etc..) on the books

# Extracted features
# Adding new books to the inventory
# Deleting books from the inventory

app = Flask(__name__)

books = [
    {'id': 1, 'title': 'Foatball', 'author': 'Lionel', 'price': 9.99},
    {'id': 2, 'title': 'Soccer', 'author': 'Messi', 'price': 7.99}
]

# Get endpoint to fetch all todo items
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify({'books':books})

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book:
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book['id'] != id]
    return "", 200

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

if __name__ == "__main__":
    app.run(port=3000)