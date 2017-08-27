Profile DB

A simple database profiler.

The purpose of this is to create a small database with 1 table and see how long it takes for Python to access the database. The purpose is not to profile the database itself, only Python attempting to access the database and pull any results into memory.

In order to do this, there are accompanying C programs that do the exact same thing as the Python programs. For the purpose of this, we can assume C runs at the speed of light. The difference between the Python time and the C time was assumed to be how long Python takes to process database results.

A black box was assumed for these tests. So, going in and modifying the source code for the databases or the libraries that access the databases was avoided.

Requirements:

This was created on Ubuntu 14.04. You will need the following with apt-get or the yum equivalents:

* virtualenv
* python-dev
* postgresql
* postgresql-contrib
* postgresql-server-dev-9.5
* sqlite3
* libsqlite3-dev

Postgresql will default to creating a directory in /var/run/postgresql. The user you run as should be able to access that directory.

To run:

Install with: `./install.sh`
Run with: `./profile.py`
