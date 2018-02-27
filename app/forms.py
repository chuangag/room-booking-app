from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, DateField, SelectMultipleField, widgets
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_login import current_user
from app.models import *
import datetime

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
    fullname=StringField('Full Name',validators=[DataRequired()])
    position=StringField('Position',validators=[DataRequired()])
    teamId=IntegerField('Team number',validators=[DataRequired()])
    teamName=StringField('Team name',validators=[DataRequired()])
    submit=SubmitField('Register')

    def validate_username(self,username):
        user=User.query.filter_by(username=self.username.data).first()
        if user is not None: # username exist
            raise ValidationError('Please use a different username.')
    
    def validate_teamId(self,teamId):
        team=Team.query.filter_by(id=teamId.data).first()
        if team is not None:
            if team.teamName!=self.teamName.data:
                raise ValidationError('Team name does not match, try again.')

class AddteamForm(FlaskForm):
    id=IntegerField('Team number',validators=[DataRequired()])
    teamName=StringField('Team name',validators=[DataRequired()])
    submit=SubmitField('Add')

    def validate_id(self,id):
        team=Team.query.filter_by(id=id.data).first()
        if team is not None:
            raise ValidationError('Team Exist, try again')
    
    def validate_teamName(self,teamName):
        team=Team.query.filter_by(teamName=teamName.data).first()
        if team is not None:
            raise ValidationError('Team Name Exist, try again') 

class AdduserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    fullname=StringField('Full Name',validators=[DataRequired()])
    position=StringField('Position',validators=[DataRequired()])
    teamId=IntegerField('Team number',validators=[DataRequired()])
    teamName=StringField('Team name',validators=[DataRequired()])
    submit=SubmitField('Register')

    def validate_username(self,username):
        user=User.query.filter_by(username=self.username.data).first()
        if user is not None: # username exist
            raise ValidationError('Please use a different username.')
    
    def validate_teamId(self,teamId):
        team=Team.query.filter_by(id=teamId.data).first()
        if team is not None:
            if team.teamName!=self.teamName.data:
                raise ValidationError('Team name does not match, try again.')

# use this so that the choice can be refreshed every time
class TeamChoiceIterable(object):
    def __iter__(self):
        teams=Team.query.all()
        choices=[(team.id,team.teamName) for team in teams] 
        choices=[choice for choice in choices if choice[1]!='Admin']
        for choice in choices:
            yield choice

class DeleteteamForm(FlaskForm):
    ids=SelectField('Choose Team',choices=TeamChoiceIterable(),coerce=int)
    submit=SubmitField('Delete')

class UserChoiceIterable(object):
    def __iter__(self):
        users=User.query.all()
        choices=[(user.id,f'{user.fullname}, team {Team.query.filter_by(id=user.teamId).first().teamName}') for user in users] 
        choices=[choice for choice in choices if 'admin' not in choice[1]] # do not delete admin
        for choice in choices:
            yield choice

class PartnerChoiceIterable(object):
    def __iter__(self):
        partners=Businesspartner.query.all()
        choices=[(partner.id,f'{partner.name} from {partner.representing}') for partner in partners] 
        #choices=[choice for choice in choices if choice[1]!='admin'] # do not delete admin
        for choice in choices:
            yield choice

class DeleteuserForm(FlaskForm):
    ids=SelectField('Choose User',coerce=int,choices=UserChoiceIterable())
    submit=SubmitField('Delete')


class RoomChoiceIterable(object):
    def __iter__(self):
        rooms=Room.query.all()
        choices=[(room.id,room.roomName) for room in rooms] 
        for choice in choices:
            yield choice

class BookmeetingForm(FlaskForm):
    title=StringField('Meeting title',validators=[DataRequired()])
    rooms=SelectField('Choose room',coerce=int,choices=RoomChoiceIterable())
    date=DateField('Choose date', format="%m/%d/%Y",validators=[DataRequired()])
    startTime=SelectField('Choose starting time(in 24hr expression)',coerce=int,choices=[(i,i) for i in range(9,19)])
    duration=SelectField('Choose duration of the meeting(in hours)',coerce=int,choices=[(i,i) for i in range(1,6)])
    participants_user=SelectMultipleField('Choose participants from company',coerce=int,choices=UserChoiceIterable(),option_widget=widgets.CheckboxInput(),widget=widgets.ListWidget(prefix_label=False),validators=[DataRequired()])
    participants_partner=SelectMultipleField('Choose participants from partners',coerce=int,choices=PartnerChoiceIterable(),option_widget=widgets.CheckboxInput(),widget=widgets.ListWidget(prefix_label=False))
    submit=SubmitField('Book')

    def validate_title(self,title):
        meeting=Meeting.query.filter_by(title=self.title.data).first()
        if meeting is not None: # username exist
            raise ValidationError('Please use another meeting title.')

    def validate_date(self,date):
        if self.date.data<datetime.datetime.now().date():
            raise ValidationError('You can only book for day after today.')
    

class MeetingChoiceIterable(object):
    def __iter__(self):
        meetings=Meeting.query.filter_by(bookerId=current_user.id).all()
        choices=[(meeting.id,f'{meeting.title} in {Room.query.filter_by(id=meeting.roomId).first().roomName} start at {meeting.date.date()} from {meeting.startTime}') for meeting in meetings] 
        for choice in choices:
            yield choice

class CancelbookingForm(FlaskForm):
    #def __init__(self,userId,**kw):
     #   super(CancelbookingForm, self).__init__(**kw)
      #  self.name.userId =userId
    ids=SelectField('Choose meeting to cancel',coerce=int,choices=MeetingChoiceIterable()) 
    submit=SubmitField('Cancel') 

class RoomavailableForm(FlaskForm):
    date=DateField('Choose date', format="%m/%d/%Y",validators=[DataRequired()])
    startTime=SelectField('Choose starting time(in 24hr expression)',coerce=int,choices=[(i,i) for i in range(9,19)])
    duration=SelectField('Choose duration of the meeting(in hours)',coerce=int,choices=[(i,i) for i in range(1,6)])
    submit=SubmitField('Check')
    
class RoomoccupationForm(FlaskForm):
    date=DateField('Choose date', format="%m/%d/%Y",validators=[DataRequired()])
    submit=SubmitField('Check')


class MeetingChoiceAllIterable(object):
    def __iter__(self):
        meetings=Meeting.query.all()
        choices=[(meeting.id,f'{meeting.title} in {Room.query.filter_by(id=meeting.roomId).first().roomName} start at {meeting.date.date()} from {meeting.startTime}') for meeting in meetings] 
        for choice in choices:
            yield choice

class MeetingparticipantsForm(FlaskForm):
    ids=SelectField('Choose meeting',coerce=int,choices=MeetingChoiceAllIterable()) 
    submit=SubmitField('Check')  
    
class CostaccruedForm(FlaskForm):
    startdate=DateField('Choose start date', format="%m/%d/%Y",validators=[DataRequired()])
    enddate=DateField('Choose end date', format="%m/%d/%Y",validators=[DataRequired()]) 
    submit=SubmitField('Check')

    def validate_enddate(self,enddate):
        if enddate.data<self.startdate.data:
            raise ValidationError('End Date must be after Start Date')