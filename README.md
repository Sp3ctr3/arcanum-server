arcanum
=======

An asymmetric encryption based file storage service.

You have to run createdb.py to construct the database first.

Running
-------
First time:
```shell
pip install -r requirements.txt
python createdb.py
```
Then on:
```shell
python server.py
```

Dependencies
------------
flask
flask-restful
flask-httpauth
flask-restful
flask-sqlalchemy
ofs
