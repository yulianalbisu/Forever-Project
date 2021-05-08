## Table of contents
* [General Information](#general-information)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)

# General Information

## Project Forever
Forever, is made especially for couples. Where they are connected through a link and can check the information of their partner, also create wishes and when the partner makes the wish comes true, the wish can be mark as done and be deleted. Users can get tips to make their relationship less monotonous and more interesting. 

## Acknowledgements
I'm very grateful to Perficent for the opportunity of learning, the completition of my dissertation would not have been possible without the support of my school of learning Hackbright Academy. 

## Author
She started a software engineering career program at Hackbright Academy, learning computer science, web developer and testing skills to perform as a software engineer as a new career. Before,  worked as an Office Administrator, prior that as a Project Supervisor, in charge of audit every project from contractor, checking and approving the budget to execute projects, as well as delivering the project on time and with the quality  specified in the bidding form. Communicate issues and delays between contractor, government and community leaders; this leaded to the Project Manager and Project Designer.  Her goal, is  to use the software skills learned for create, interact and deliver  projects, plan and interact with the clients and the necessities.

- [@yulianalbisu](https://www.github.com/yulianalbisu)
  
## API/datasets used
App was made from web scrapping to fill the data and mostly for learning purposes
  
## Badges

Database: [dbdiagram.io](https://dbdiagram.io/d/606b32b8ecb54e10c33ec030)

[![MIT License](https://raw.githubusercontent.com/graingert/WOW/master/LICENSE)]
  
  
## Documentation

[Project Details](https://www.dropbox.com/scl/fi/5odq6i954lz0qe02hnixy/My-Project.paper?dl=0&rlkey=ybvqfx3t03htvm36iqxmkv186)
 
## Features

### Landing Page
User can register, login or register partner on the landing page, also get a little description of the app. Animation made with AJAX.
![App Screenshot](/static/css/img/landingPage.png)

### User's Link
First user is provided with a link to share with the partner and be connected, to do this SQLAlchemy was needed to query from the database, PostgreSQL to build the tables and send a response using a jinja template.


### Partner's Connection
Partner can register, following the same steps as first user. Users now are using the same link with different ID's. 
![App Screenshot](/static/css/img/partnerAccount.png)

### Welcome Page
Users get a view description about relationships. The pin note has been animated and targeted using CSS.animation, AJAX and DOM manipulation, when clicked  displays a pop-up containing a compliment for the users.
![caption](/static/css/img/welcomePage/GIF)

### Menu Display Effect
When "Menu" is clicked, it opens a sidebar and makes visible an overlay layer, includes a collapsible part where user can navigate to the different content of Forever App. Using Bootstrap component, animate.css, wow.js, Backstrectch, CSS Media Queries, jQuery and Javascript to target the objects. 
![App Screenshot](/static/css/img/sideBar.png)

### Love Quiz
Users filled a form about personal questions, when submitted partner can view the loved one information and know about the favorite stuff, answer can be updated anytime and user can come back later and view which questions need to be answered. I used SQLAlchemy querying the database, together with  to be able to update the database, this sent in a Jinja template.
![App Screenshot](/static/css/img/questions.png)

### Make a Wish
Couple can write something they would like to do or have and their partner can view on dashboard the wish and when wish comes true can be marked as done and deleted, getting ready for the next one. Request made with Jinja and event handling with jQuery.
![App Screenshot](/static/css/img/wishes.png)

### View Answers and Wishes
After users finish the Love Quiz or Make a Wish they get a response of the recent data filed. An inner join is made as well as a left join. After the love quiz, answers appeared and this effect is handling with querySelector, manipulation of the DOM
![App Screenshot](/static/css/img/wishes.png)

### Tips
Users can click on circle buttons and get tips of how to get closer to partner and why knowing about partner favorite things are useful to grow together in the relationship. Request made with Jinja on a data scrapping json file. 


## Feedback

If you have any feedback, please reach out to us at linkedIn: Yuliana Aldrich
  
## Lessons Learned

Relationships from the database and their importance, how to query data, manage users and save their data, sessions, cookies, responsive design, get and post requests using Python3 and Java Script.
Some challenges I faced were getting the relationships many to many and one to many as well as making the sidebar animated with effect on background in the main html.
Overcoming some with advisor help and others reading and scrapping around the web and documentation in Spanish, my native language. 
![App Screenshot](/static/css/img/dbmodel.png)

## Optimizations

Refactors, performance improvements, looking forward to make it accessible in spanish language.
 
  
## Run Locally

Clone the project

```bash
  git clone https://https://github.com/yulianalbisu/Forever-Project
```

Go to the project directory

```bash
  cd forever-project
```

```bash
  virtualenv env
```
```bash
  source env/bin/activate
```

Install requirements

```bash
  pip3 install requirements.txt
```

```bash
  sudo service postgresql 
```
Start the server

## Technologies
Technologies used on this project:
* Python3
* PostgresQL
* SQLAlchemy
* Flask
* Jinja2
* JQuery
* Backstretch plugin
* JavaScript
* Dom Manipulation
* Event Handling
* Ajax
* CSS
* CSS Media Queries
* Animate from CSS
* HTML
* Bootstrap 

## Future State
-Translation to Spanish
- Share playlist songs
- Find a nanny for daynight
- Play a game getting brownie points

## Looking forward
To apply some new features using:
* REACT
  
## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

  