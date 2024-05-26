from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, Schedule, User
from datetime import datetime

schedule_bp = Blueprint('schedule', __name__)

@schedule_bp.route('/get-schedule', methods=['POST'])
@jwt_required()
def get_schedule():
    data = request.get_json()
    date = datetime.strptime(data['date'], '%Y-%m-%d')
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    # Assuming you have a Schedule model and it has a date field
    schedules = Schedule.query.filter_by(user_id=user_id, date=date).all()

    schedule_list = [
        {
            "time": schedule.time,
            "room": schedule.room,
            "subject": schedule.subject,
            "group": schedule.group
        }
        for schedule in schedules
    ]

    return jsonify(schedule_list), 200
