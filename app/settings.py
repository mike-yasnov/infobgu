from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, User

settings_bp = Blueprint('settings', __name__)

@settings_bp.route('/change_password', methods=['POST'])
@jwt_required()
def change_password():
    data = request.get_json()
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    user.password = generate_password_hash(data['new_password'], method='sha256')
    db.session.commit()
    return jsonify({'message': 'Password changed successfully'})
