from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    schedules = db.relationship('Schedule', backref='user', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
        }

class Folder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('folders', lazy=True))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id,
        }

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    folder_id = db.Column(db.Integer, db.ForeignKey('folder.id'), nullable=False)
    folder = db.relationship('Folder', backref=db.backref('files', lazy=True))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'folder_id': self.folder_id,
        }

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    score = db.Column(db.Integer, default=0)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'score': self.score,
        }

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.String(50), nullable=False)
    room = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    group = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'subject': self.subject,
            'group': self.group,
            'user_id': self.user_id,
        }
