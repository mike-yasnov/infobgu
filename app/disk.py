from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, Folder, File

disk_bp = Blueprint('disk', __name__)

@disk_bp.route('/folders', methods=['POST'])
@jwt_required()
def create_folder():
    data = request.get_json()
    user_id = get_jwt_identity()
    new_folder = Folder(name=data['name'], user_id=user_id)
    db.session.add(new_folder)
    db.session.commit()
    return jsonify({'message': 'Folder created successfully'})

@disk_bp.route('/folders', methods=['GET'])
@jwt_required()
def get_folders():
    user_id = get_jwt_identity()
    folders = Folder.query.filter_by(user_id=user_id).all()
    return jsonify([folder.serialize() for folder in folders])

@disk_bp.route('/files', methods=['POST'])
@jwt_required()
def upload_file():
    data = request.get_json()
    new_file = File(name=data['name'], folder_id=data['folder_id'])
    db.session.add(new_file)
    db.session.commit()
    return jsonify({'message': 'File uploaded successfully'})

@disk_bp.route('/files', methods=['GET'])
@jwt_required()
def get_files():
    user_id = get_jwt_identity()
    files = File.query.filter_by(user_id=user_id).all()
    return jsonify([file.serialize() for file in files])
