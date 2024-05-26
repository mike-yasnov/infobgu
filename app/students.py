from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, Student

students_bp = Blueprint('students', __name__)

@students_bp.route('/', methods=['GET'])
@jwt_required()
def get_students():
    students = Student.query.all()
    return jsonify([student.serialize() for student in students])

@students_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_student(id):
    data = request.get_json()
    student = Student.query.get_or_404(id)
    student.score = data.get('score', student.score)
    db.session.commit()
    return jsonify({'message': 'Student updated successfully'})
