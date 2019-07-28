to configure python for flask and database :
'''
pip install -r requirements.txt
'''
to run unit tests [it will create a database and tear it down]:
'''
python manage.py test
'''
to run the project [the project checks if database is configured if not it will configure it before running]:
'''
python manage.py run
'''
