# pool_and_resources

configure python for flask and database :

```
pip install -r requirements.txt
```

configure the database using database.sql file content then do the manage steps:

```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

to run unit tests that assumes that database already set and everything is ready : 

```
python tests.py
```

then to run the application use the following : 
```
python manage.py runserver
```

