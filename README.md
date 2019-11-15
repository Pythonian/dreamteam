Host on PythonAnywhere
======================

> Start a new Bash console

* Clone the repository from github `git clone https://github.com/Pythonian/dreamteam.git`
* Create a virtualenv `mkvirtualenv dreamteam` and activate it
* Change into the folder directory `cd dreamteam`
* Install the dependencies with the command `pip install -r requirements.txt`

> Now, in the Web tab on your dashboard

* Create a new web app
* Select Manual configuration
* Once web app is created, enter the name of the virtualenv you created

> Database Configuration

* In the database tab, set a new password and then initialize a MySQL server
* Create a new database or use the default database

> Migrating the database

* Return to the bash console and run the following commands while in virtualenv

``` bash
> (venv) export FLASK_CONFIG=production
> (venv) export FLASK_APP=wsgi.py
> (venv) export SQLALCHEMY_DATABASE_URI='mysql://your-username:your-password@db-host-address/your-database-name'
> (venv) flask db init
> (venv) flask db migrate
> (venv) flask db upgrade
```

> WSGI file

* Navigate to the Code section of the Web tab
* Edit the WSGI configuration file with the following contents:

``` python
import os
import sys

path = '/home/your-username/your-project-directory-name'
if path not in sys.path:
    sys.path.append(path)

os.environ['FLASK_ENV'] = 'production'
os.environ['SECRET_KEY'] = 'p9Bv<3Eid9%$i01'
os.environ['SQLALCHEMY_DATABASE_URI'] = 'mysql://your-username:your-password@your-host-address/your-database-name'

from wsgi import app as application
```

> Push your changes to version control, and pull them on the PythonAnywhere Bash console:

``` bash
git pull origin master
```

> To create an admin user locally, open the bash console and type in the following:

``` bash
$ (venv) flask shell
>>> admin = Employee(email="admin@gmail.com", username="admin", password="admin", is_admin=True)
>>> db.session.add(admin)
>>> db.session.commit()
```

> Launching the App

* Reload the app on the Web tab
* Then go to the app URL
