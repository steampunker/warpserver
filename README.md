AlbianWarp Server
==========

Albian Warp is a community replacement for the long-defunct Docking Station multiplayer Functionality.

Features
--------

* User Handling (Registration & Authentication)


Dependencies
------------

* [Python 2.7](http://www.python.org/) <i>(NOT Python3)</i>
* [Flask 0.10.1](http://flask.pocoo.org/docs/0.10/)
* [Flask-SQLAlchemy 2.0](https://pythonhosted.org/Flask-SQLAlchemy/index.html)
* [Flask-RESTful](https://flask-restful.readthedocs.org/en/0.3.1/)
* [Passlib 1.6.2](https://pythonhosted.org/passlib/)

Tested and confirmed as working on Linux 32-bit, 64-bit

Usage
-----

Run this command, to Initialize the Database & Tables!

	python server.py initdb

To Start the Server, with Flasks standart WSGI Server (werkzeug), run this command:

	python server.py run

If you ever need to drop all the Database Tables use:

	python server.py dropdb