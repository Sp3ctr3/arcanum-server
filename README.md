arcanum
=======

An asymmetric encryption based file storage service. In Arcanum, the server plays very little role. The client handles encryption as well as decryption. The server merely handles file storage and user management. This ensures that even if the server is compromised, the user data is not.

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
