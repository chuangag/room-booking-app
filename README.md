Product Requirements
 
Author(s): Afua Achee Ryan Cooper, Jon

Related Documents

Related Links


Context	2
Product Benefits	2
Product Goals	2
Hypothesis/Assumptions	2
Partnering Teams	3
Product Considerations	3
Product Questions	3
Product Decisions	3
Product Implementation	3
P0	4
P1	4
Design Files	4
Metrics	4
Challenges	4
Launch Plan	4
Go-To-Market Links	5
Appendix	5


Context
Include an introduction to the overall product initiative.  This will include the targeted users, the problem statement and a brief overview of why you are solving the problem.  This can mirror the same introduction that you have written in your Weekly Update Template. 

COVID-19 has disrupted the American way of life, excluding citizens from being able to enjoy one of their favorite activities, eating out. However, as Americans begin to adapt to the new COVID_concerned environment, the task can be anxiety-provoking. Therefore, to ease this anxiety, we plan to create a tool that will empower Americans to return to their New Normal, while still relishing the activities of the past.


“How might we” statement - After describing the problem statement and why you are solving the problem, you can include the “How might we” statement. For those unfamiliar with design thinking, the “How might we” statement focuses on describing how you can turn the problem statement into a solution that you can provide for your members by giving a high level overview of what the solution would be.  Check out this site to learn more about the “How might we” statement.

How might we create a COVID-friendly dining experience?
How might we make everyone feel included within the dining environment?
Although socially-distant, how might we provide an opportunity for camaraderie?

How might we assist servers in doing their job in a COVID-friendly way?
How might we decrease the amount of face-to-face communication between the servers and their guests?
Product Benefits
This will be a detailed list of the expected benefits that will come from solving this problem
Faster dining experience - food orders are placed prior to entering the restaurant, food is prepared “just-in-time”
Safer Dining Experience - servers can focus more on sanitation of the environment
Tastier Dining Experience - with patrons placing orders via an online RSVP channel, there will be less errors in the process of ordering food

Product Goals
List of goals that you want your members to accomplish with the implementation of the feature.  This list will eventually turn into a feature list that you will implement in the phases described in the “Product Implementation” section.  These goals are fairly high level given that, at the time you wrote the PRD, you most likely have not had detailed discussions on HOW these could be implemented.

Goal: create a RSVP system where patrons can reserve a table and order their food with personal requests via phone
Goal: enable restaurant staff to be able to monitor food inventory levels via mobile devices
Future Goal: allow users to record orders via audio. Have audio transcription to be able to translate the order

Hypothesis/Assumptions
List the hypothesis and/or assumptions that you are making about the market, the target user, or the solution itself

Servers would be willing to communicate mainly with their patrons through mobile devices
Users would be willing to direct the majority of their dining experience through mobile devices
Restaurants would be more efficient if traffic could be monitored/ accounted for mainly based on mobile device


Product Considerations
List all of the design, engineering and product considerations that may affect your product development.  This could be edge cases with respect to how you expect members to receive the product.  This could be preliminary answers that answer how some aspect of your solution will be completed.

Ex.
Engineering has to complete all work within the quarter due to limited resourcing next quarter
All downstream products must be able to digest the new information collected from the member

Product Questions followed by Product Decisions
We want to make an app that will allow us to do bookings/ RSVPS.
Should we make a web app, or a mobile application?
We should make a web app. It is less complicated, but more so allows for universal access regardless of the client-side device.



Product Implementation
This lists the phased approach about how all of the product goals listed in the Context section will be delivered

P0
Goal: enable member to be able to record a message on their phone
Goal: Enable member to be able to listen to message on mobile and desktop devices

P1
Goal: Enable members to share the message with other members.


Design Files
Links to all of the design files associated with the product

Metrics
List of all metrics associated with the product.
Challenges
List of all expected challenges that may occur during and after the product development.  These could be user adoption challenges or internal design, product, or engineering challenges
Launch Plan
Tomorrow

Go-To-Market Links
None Yet : https://hackgsu-fall2020.devpost.com/
Appendix
List of additional information that may help provide context but that wasn’t 100% necessary to be included in the sections above.  You can also included outdated information




Product : A restaurant booking system
=====
The web application is build with python Flask framwork along with SQLite3 database. It has basic login system since the booking have to be done with authentication. A admin account is created by default, with username: admin, and password: admin. The administrator have the access to directly manipulate team and users. 

## Requirements
1. Python 3.6, recommending [Anaconda](https://anaconda.org/anaconda/python)
2. Install SQLite3 from [Here](http://www.sqlite.org/download.html)
3. Recommend SQLite browser [Available](http://sqlitebrowser.org/)

## Setup
1. Install flask and packages
```
$ pip install flask
$ pip install flask-wtf
$ pip install flask-sqlalchemy
$ pip install flask-migrate
$ pip install flask-login
```
2. Define the project
```
$ export FLASK_APP=lab2.py
```

3. Init the database
```
$ flask db init
```

## Migrating data
1. Run the migration command from the project directory to create tables
```
$ flask db upgrade
```
2. Populate the database with dummy data(if weren't populated after migration)
```
$ python populate.py
```

# Running
1. Run the flask application from the project directory, running on localhost
```
$ flask run
```
2. Open the app in browser: [localhost](http://127.0.0.1:5000/)
