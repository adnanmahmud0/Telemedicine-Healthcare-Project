<h1> Telemedicine & Healthcare Project </h1>

The Telemedicine application aims to provide a convenient and accessible platform for users to seek medical assistance remotely. By utilizing chatbot technology, disease detection algorithms, and integration with external services, the application will enhance the overall healthcare experience for users. 

This website run by the Django framework.

Django version 4.2.1, Python verson 3.11

The website database connect with Xampp.


If you want to run the project then you need to 
1) install python
2) open the Telemedicine file with VS code or PyCharm
3) In the VS or Pycharm open the terminal
4) type "cd mysite" and press enter
5) In the terminal install Django(pip install django) and Mysqlclient(pip install mysqlclient)
5) Oprn Xampp and create database and copy the database name
6) Open the settings.py file (the file is in the mysite folder),
   go to the DATABASES code and change the database name that was copyed
7) In the terminal type "python manage.py makemigrations" and press enter
8) Again type "python manage.py migrate" and press enter. Done database connected
9) In the terminal type "python manage.py createseperuser" to create superuser for admin site
10) enter your username, email, password and confirm password(when typing password you can't see the password)
11) Done all the setup
12) To start the project type in the terminal "python manage.py runserver"
13) You will get the localhost ip. Click the ip to see the website
14) Signup and then login the website
