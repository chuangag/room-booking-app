from flask import render_template, flash, redirect, request, url_for
from werkzeug.urls import url_parse
from app import app
from app.forms import *
from flask_login import current_user, login_user, logout_user, login_required
from app.models import *
from app import db
import sqlite3

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page=request.args.get('next')
        if not next_page or url_parse(next_page).netloc!='':
            next_page=url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form =RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,\
                  fullname=form.fullname.data,\
                  position=form.position.data,\
                  teamId=form.teamId.data)
        user.set_password(form.password.data)
        db.session.add(user)
        team=Team.query.filter_by(id=user.teamId).first()
        if team is None:
            newTeam=Team(id=user.teamId,\
                         teamName=form.teamName.data)
            db.session.add(newTeam)
            db.session.commit()
            flash('Registered with a new team created')
            return redirect(url_for('login'))
        else:
            db.session.commit()
            flash('Registered to an existing team')
            return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)

@app.route('/adduser', methods=['GET','POST'])
@login_required
def adduser():
    if not current_user.is_authenticated:
        flash('Please Log in as admin to add user')
        return redirect(url_for('login')) 
    if current_user.username!='admin':
        flash('Please Log in as admin to add user')
        return redirect(url_for('index'))
    form =AdduserForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,\
                  fullname=form.fullname.data,\
                  position=form.position.data,\
                  teamId=form.teamId.data)
        user.set_password(form.password.data)
        db.session.add(user)
        team=Team.query.filter_by(id=user.teamId).first()
        if team is None:
            newTeam=Team(id=user.teamId,\
                         teamName=form.teamName.data)
            db.session.add(newTeam)
            db.session.commit()
            flash(f'Added user {form.username.data} with a new team created')
            return redirect(url_for('adduser'))
        else:
            db.session.commit()
            flash(f'Added user {form.username.data} to an existing team')
            return redirect(url_for('adduser'))
    return render_template('adduser.html',title='Add User',form=form)

@app.route('/addteam',methods=['GET','POST'])
@login_required
def addteam():
    if not current_user.is_authenticated:
        flash('Please Log in as admin to add team')
        return redirect(url_for('login')) 
    if current_user.username!='admin':
        flash('Please Log in as admin to add team')
        return redirect(url_for('index'))
    form=AddteamForm()
    if form.validate_on_submit():
        team=Team(id=form.id.data,\
                  teamName=form.teamName.data)
        db.session.add(team)
        db.session.commit()
        flash(f'Team {form.teamName.data} successfully added!')
        return redirect(url_for('addteam'))
    return render_template('addteam.html',title='Add Team',form=form)
        
@app.route('/deleteteam',methods=['GET','POST'])
@login_required
def deleteteam():
    if not current_user.is_authenticated:
        flash('Please Log in as admin to delete team')
        return redirect(url_for('login')) 
    if current_user.username!='admin':
        flash('Please Log in as admin to delete team')
        return redirect(url_for('index'))
    form=DeleteteamForm()
    
    if form.validate_on_submit():
        team=Team.query.filter_by(id=form.ids.data).first()

        meetings=Meeting.query.filter_by(teamId=team.id).all()
        hasFutureBooking=False
        for meeting in meetings:
            if meeting.date>datetime.now():
                hasFutureBooking=True
                break
        if hasFutureBooking:
            flash('You cannot delete a team that holds future bookings!')
            return redirect(url_for('deleteteam'))

        # delete all users in a deleted team
        userInTeam=User.query.filter_by(teamId=form.ids.data).all()
        for user in userInTeam:
            db.session.delete(user)
        db.session.delete(team)
        db.session.commit()
        flash(f'Team {team.teamName} and team members successfully deleted! Please register member again to other team')
        return redirect(url_for('index'))
    form=DeleteteamForm()
    return render_template('deleteteam.html',title='Delete Team',form=form)

@app.route('/deleteuser',methods=['GET','POST'])
@login_required
def deleteuser():
    if not current_user.is_authenticated:
        flash('Please Log in as admin to delete user')
        return redirect(url_for('login')) 
    if current_user.username!='admin':
        flash('Please Log in as admin to delete user')
        return redirect(url_for('index'))
    
    form=DeleteuserForm()
    if form.validate_on_submit():
        user=User.query.filter_by(id=form.ids.data).first()

        meetings=Meeting.query.filter_by(bookerId=user.id).all()
        hasFutureBooking=False
        for meeting in meetings:
            if meeting.date>datetime.now():
                hasFutureBooking=True
                break
        if hasFutureBooking:
            flash('You cannot delete a user that holds future bookings!')
            return redirect(url_for('deleteuser'))

        db.session.delete(user)
        db.session.commit()
        flash(f'User {user.username} successfully deleted! ')
        return redirect(url_for('index'))
    return render_template('deleteuser.html',title='Delete User',form=form)

@app.route('/book',methods=['GET','POST'])
@login_required
def book():
    form=BookmeetingForm()
    if form.validate_on_submit():
        # check time collision
        pass

        # make booking
        booker=current_user
    
        team=Team.query.filter_by(id=current_user.teamId).first()
        room=Room.query.filter_by(id=form.rooms.data).first()
        cost=room.cost
        endTime=form.startTime.data+form.duration.data
        ### only user can be participant currently
        participants_user=form.participants_user.data

        meeting=Meeting(title=form.title.data,teamId=team.id,roomId=room.id,bookerId=booker.id,date=form.date.data,startTime=form.startTime.data,endTime=endTime,duration=form.duration.data)
        db.session.add(meeting)

        # Add booking log
        log=CostLog(title=form.title.data,teamId=team.id,teamName=team.teamName,date=form.date.data,cost=cost*form.duration.data)
        db.session.add(log)

        # Add participants records(currently only user)
        for participant in participants_user:
            participating=Participants_user(meeting=form.title.data,userId=participant)
            db.session.add(participating)
        db.session.commit()
        flash('Booking success!')
        return redirect(url_for('index'))
    return render_template('book.html',title='Book Meeting',form=form)
