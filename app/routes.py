from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import User, Folder, File
from . import db

disk_bp = Blueprint('disk', __name__)

@disk_bp.route('/folders', methods=['POST'])
@jwt_required()
def create_folder():
    data = request.get_json()
    folder_name = data.get('name')
    user_id = get_jwt_identity()
    new_folder = Folder(name=folder_name, user_id=user_id)
    db.session.add(new_folder)
    db.session.commit()
    return jsonify({'message': 'Folder created successfully'}), 201

# Implement other routes for disk, students, schedule, settings similarly
