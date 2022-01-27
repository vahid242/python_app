How operate with PostgreSQL in Flask with SQLAlchemy:

1. SQLAlchemy is based on psycopg2, install 
on mac : pip3 install psycopg2-binary psycopg2
on windowds: pip3 install psycopg2

2.  pip3 install wheel

3. 
on mac: pip3 install flask-sqlalchemy
on windowds: 
	a. download psycopg2..._win32/64.whl
	b. copy file where runing the code 
	c. pip3 install flask-sqlalchemy
	
4. in the program (python script) impoert SQLAlchemy:
from flask_sqlalchemy import SQLAlchemy