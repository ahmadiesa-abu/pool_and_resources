to configure python for flask and database :
```
pip install -r requirements.txt
```
to setup database environment variable :
```
set DB_USERNAME=[database username]
set DB_PASSWORD=[database password]
set DB_HOST=[database host-name/ip]
set DB_PORT=[database listening port]
set DB_NAME=[database name]

```
to run unit tests [it will create a database and tear it down]:
```
python manage.py test
```
to run the project [the project checks if database is configured if not it will configure it before running]:
```
python manage.py run
```
