from app import app,db
from datetime import datetime
from app.models import *

# add team
team=Team(id=1,teamName='Admin')
db.session.add(team)
team=Team(id=2,teamName='Manage')
db.session.add(team)
team=Team(id=3,teamName='Ops')
db.session.add(team)
team=Team(id=4,teamName='Dev')
db.session.add(team)
team=Team(id=5,teamName='HR')
db.session.add(team)
team=Team(id=6,teamName='Market')
db.session.add(team)

# add admin & users
user=User(id=1,username='admin',fullname='admin',position='admin',teamId=1)
user.set_password('admin')
db.session.add(user)

user=User(id=2,username='apple',fullname='Apple',position='CEO',teamId=2)
user.set_password('apple')
db.session.add(user)
user=User(id=3,username='bob',fullname='Bob',position='CTO',teamId=4)
user.set_password('bob')
db.session.add(user)
user=User(id=4,username='cat',fullname='Cat',position='employee',teamId=3)
user.set_password('cat')
db.session.add(user)
user=User(id=5,username='dave',fullname='Dave',position='pm',teamId=4)
user.set_password('dave')
db.session.add(user)

# add rooms
room=Room(id=1,roomName='room1',telephone=True,projector=True,whiteboard=True,cost=500)
db.session.add(room)
room=Room(id=2,roomName='room2',telephone=False,projector=True,whiteboard=True,cost=300)
db.session.add(room)
room=Room(id=3,roomName='room3',telephone=False,projector=False,whiteboard=True,cost=100)
db.session.add(room)
room=Room(id=4,roomName='room4',telephone=False,projector=False,whiteboard=True,cost=100)
db.session.add(room)

# add past meetings
meeting=Meeting(id=9,title='past meeting',teamId=3,roomId=2,bookerId=2,date=datetime(2018,2,15),startTime=10,endTime=14,duration=4)
db.session.add(meeting)

# add past meeting cost log
costlog=CostLog(id=10,teamId=4,teamName='Dev',title='past meeting',date=datetime(2018,2,15),cost=1200)
db.session.add(costlog)

# add business partners
partner=Businesspartner(id=1,name='Zeus',representing='Thunder electricity',position='CEO')
db.session.add(partner)
partner=Businesspartner(id=2,name='Yan',representing='Facebook',position='CTO')
db.session.add(partner)
partner=Businesspartner(id=3,name='Xanos',representing='Avengers',position='Boss')
db.session.add(partner)

db.session.commit()