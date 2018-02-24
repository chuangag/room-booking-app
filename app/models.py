from datetime import datetime
from app import db
# currently might not use in this simple project, do migration manually using
# SQL queries
class User(db.Model):
    userId=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name=db.Column(db.String(64), nullable=False)
    password_hash=db.Column(db.String(64), nullable=False)
    position=db.Column(db.String(64), nullable=False)
    teamId=db.Column(db.Integer, db.ForeignKey('team.teamId'), nullable=False)
    meetings=db.relationship('Meeting',backref='booker',lazy='dynamic')
    participatings=db.relationship('Participants_user',backref='participater',lazy='dynamic')

    def __repr__(self):
        return f'<User {self.name}>'

class Team(db.Model):
    teamId=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    teamName=db.Column(db.String(64), nullable=False,unique=True)
    members=db.relationship('User',backref='team',lazy='dynamic')
    meetings=db.relationship('Meeting',backref='team',lazy='dynamic')

    def __repr__(self):
        return f'<Team {self.teamName}>'

class Businesspartner(db.Model):
    partnerId=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name=db.Column(db.String(64), nullable=False)
    representing=db.Column(db.String(64), nullable=False)
    position=db.Column(db.String(64), nullable=False)
    participatings=db.relationship('Participants_partner',backref='participater',lazy='dynamic')

    def __repr__(self):
        return f'BusinessPartner {self.name}'

class Room(db.Model):
    roomId=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    roomName=db.Column(db.String(64), nullable=False)
    telephone=db.Column(db.Boolean,nullable=False)
    projector=db.Column(db.Boolean,nullable=False)
    whiteboard=db.Column(db.Boolean,nullable=False)
    location=db.Column(db.String(64),nullable=False)
    cost=db.Column(db.Integer, nullable=False)
    meetings=db.relationship('Meeting',backref='room',lazy='dynamic')
    
    def __repr__(self):
        return f'Room {self.roomName}'

class Meeting(db.Model):
    meetingId=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    teamId=db.Column(db.Integer, db.ForeignKey('team.teamId'), nullable=False)
    roomId=db.Column(db.Integer, db.ForeignKey('room.roomId'), nullable=False)
    bookerId=db.Column(db.Integer, db.ForeignKey('user.userId'), nullable=False)
    startTime=db.Column(db.DateTime,nullable=False)
    endTime=db.Column(db.DateTime,nullable=False)
    duration=db.Column(db.Integer,nullable=False)
    cost=db.Column(db.Integer,nullable=False)
    participants_user=db.relationship('Participants_user',backref='meeting',lazy='dynamic')
    participants_partner=db.relationship('Participants_partner',backref='meeting',lazy='dynamic')

    def __repr__(self):
        return f'Meeting {self.meetingId} for {self.teamId} last for {self.duration}'

class Participants_user(db.Model):
    dummyId=db.Column(db.Integer,primary_key=True)
    meetingId=db.Column(db.Integer, db.ForeignKey('meeting.meetingId'), nullable=False)
    userId=db.Column(db.Integer, db.ForeignKey('user.userId'), nullable=False)

class Participants_partner(db.Model):
    dummyId=db.Column(db.Integer,primary_key=True)
    meetingId=db.Column(db.Integer, db.ForeignKey('meeting.meetingId'), nullable=False)
    partnerId=db.Column(db.Integer, db.ForeignKey('businesspartner.partnerId'), nullable=False)




