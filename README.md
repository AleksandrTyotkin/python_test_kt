# python_test_kt

Тестовая форма для проверки работы Flask фраемворка и средствами работы с БД - SQLAlchemy
разрабатывалась и тестировалась на Win10 / Python 3.9.5 / Google Chrome версия 90.0.4430.212 (Официальная сборка), (64 бит)

Using:

click==7.1.2
Flask==1.1.2
Flask-SQLAlchemy==2.5.1
greenlet==1.1.0
gunicorn==20.1.0
itsdangerous==1.1.0
Jinja2==2.11.3
MarkupSafe==1.1.1
migrate==0.3.7
SQLAlchemy==1.4.14
Werkzeug==1.0.1

/////////////////////////

For running project start up virtual environment to you system:

using: 

for nix
python -m pip install -r requirements.txt 

for win
virtualenv

/////////////////////////

How to install virtualenv:
Install pip first

  sudo apt-get install python3-pip
  
Then install virtualenv using pip3

  sudo pip3 install virtualenv
  
Active your virtual environment:  

  source env/Scripts/activate
  
To deactivate:

  deactivate
  
/////////////////////////

For start project in winOS:

  sourse python app.py
  
  
'''
(env) C:\ktest>python app.py
C:\ktest\env\lib\site-packages\flask_sqlalchemy\__init__.py:872: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
C:\ktest\env\lib\site-packages\flask_sqlalchemy\__init__.py:872: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
 * Debugger is active!
 * Debugger PIN: 214-392-521
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 '''
 
/////////////////////////
 
 Go to your browser, 
 and running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 
 /////////////////////////
 
 Aleksandr Tyotkin
 
