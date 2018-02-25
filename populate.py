from app import app,db
from app.models import *

# add team
team=Team(id=9999,teamName='Admin')
db.session.add(team)
team=Team(id=1,teamName='Manage')
db.session.add(team)
team=Team(id=2,teamName='Ops')
db.session.add(team)
team=Team(id=3,teamName='Dev')
db.session.add(team)
team=Team(id=4,teamName='HR')
db.session.add(team)
team=Team(id=5,teamName='Market')
db.session.add(team)

# add admin & users
user=User(id=9999,username='admin',fullname='admin',position='admin',teamId=9999)
user.set_password('admin')
db.session.add(user)

user=User(id=1,username='apple',fullname='Apple',position='CEO',teamId=1)
user.set_password('apple')
db.session.add(user)
user=User(id=2,username='bob',fullname='Bob',position='CTO',teamId=3)
user.set_password('bob')
db.session.add(user)
user=User(id=3,username='cat',fullname='Cat',position='employee',teamId=2)
user.set_password('cat')
db.session.add(user)
user=User(id=4,username='dave',fullname='Dave',position='pm',teamId=3)
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

db.session.commit()