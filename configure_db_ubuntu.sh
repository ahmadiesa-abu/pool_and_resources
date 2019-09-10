#!/bin/bash

sudo apt-get install -y postgresql postgresql-contrib python-pip python-psycopg2 libpq-dev python-dev libxml2-dev libxslt-dev libffi-dev
update-rc.d postgresql enable
service postgresql start
sudo echo "postgres" | sudo passwd --stdin postgres
sudo echo "postgres" | su - postgres -c "psql -c \"create database pools;\""
sudo echo "postgres" | su - postgres -c "psql -c \"create user pools with password 'pool1234';\""
sudo echo "postgres" | su - postgres -c "psql -c \"grant all privileges on database pools to pools;\""
