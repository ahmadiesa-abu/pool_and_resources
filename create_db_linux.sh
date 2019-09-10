#!/bin/bash
sudo yum update
sudo yum install -y postgresql-server postgresql-contrib python-psycopg2 python-devel postgresql-devel python-pip
sudo yum groupinstall -y "Development Tools"
sudo postgresql-setup initdb
sudo sed -i 's/ident/trust/g' /var/lib/pgsql/data/pg_hba.conf
sudo systemctl enable postgresql
sudo systemctl start postgresql
sudo echo "postgres" | sudo passwd --stdin postgres
sudo echo "postgres" | su - postgres -c "psql -c \"create database pools;\""
sudo echo "postgres" | su - postgres -c "psql -c \"create user pools with password 'pool1234';\""
sudo echo "postgres" | su - postgres -c "psql -c \"grant all privileges on database pools to pools;\""
