from flask import Blueprint, request, jsonify
from models import Note, db

notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/', methods=['GET'])
def get_notes():
    notes = Note.query.all()
    return jsonify([{'id': n.id, 'title': n.title, 'content': n.content} for n in notes])

@notes_bp.route('/', methods=['POST'])
def create_note():
    data = request.get_json()
    note = Note(title=data['title'], content=data['content'])
    db.session.add(note)
    db.session.commit()
    return jsonify({'id': note.id, 'title': note.title, 'content': note.content})

@notes_bp.route('/<int:id>', methods=['PUT'])
def update_note(id):
    data = request.get_json()
    note = Note.query.get_or_404(id)
    note.title = data['title']
    note.content = data['content']
    db.session.commit()
    return jsonify({'id': note.id, 'title': note.title, 'content': note.content})

@notes_bp.route('/<int:id>', methods=['DELETE'])
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return jsonify({'message': 'Deleted'})
