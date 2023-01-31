# Dating wesite
This is a sample application that demonstrates an dating website using the Python Django. The application loads Profil from a PostgreSQL database and displays them. Users can select to display profile and send them request. Users can register and login to website and, click on any profile to get more information after accepting request, User can view profile view. Users can select profile and add to liked profiles,and try to contact using inbuilt messaging app. They can view profile likes, User can purchase subscription using rozerpay. In admin side, admins can manage users,profiles,payment history,liked profiles, etc...

# Getting Started
To get started you can simply clone this youandme repository and install the dependencies.

Clone the youandme repository using git:
```
git clone https://github.com/noufida/ecommerce-django.git
cd ecommerce-django
```
Create a virtual environment to install dependencies in and activate it:

```
python3 -m venv env
source env/bin/activate
```
Then install the dependencies:

```
(env)$ pip install -r requirement.txt
```
Note the ```(env)```in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once ```pip``` has finished downloading the dependencies:

```
(env)$ cd ecommerce-django
(env)$ python3 manage.py runserver
```

And navigate to ```http://127.0.0.1:8000/```

# Tech Stack

Python

Django

PostgreSQL

Bootstrap

Javascript

Web socket
