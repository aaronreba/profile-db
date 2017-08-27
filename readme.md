Profile DB

A simple database profiler.

The purpose of this is to create a small database with 1 table and see how long it takes for Python to access the database. The purpose is not to profile the database itself, only Python attempting to access the database.

Requirements:

This was created on Ubuntu 14.04. You will need the following with apt-get or the yum equivalents:

virtualenv
python-dev
postgresql
postgresql-contrib
postgresql-server-dev-9.5
sqlite3
libsqlite3-dev

Postgresql will default to creating a directory in /var/run/postgresql. The user you run as should be able to access that directory.

To run:

Install with: `./install.sh`
Run with: `./profile.py`
