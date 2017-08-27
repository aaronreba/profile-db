#!/bin/bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pushd $DIR > /dev/null

mkdir -p log
mkdir -p db

# make pyenv

if [ -d pyenv ]; then
  echo "Not creating virtualenv. Already exists."
else
  /usr/bin/virtualenv pyenv
  pyenv/bin/pip install -r requirements.pip
  echo "Created virtualenv database."
fi

#postgres database

if [ -d db/pg_db ]; then
  echo "Not creating postgres database. Already exists."
else
  /usr/lib/postgresql/9.5/bin/initdb -D db/pg_db -U postgres
  /usr/lib/postgresql/9.5/bin/pg_ctl -D db/pg_db -o "-p 1115" -l log/pg_logfile start
  sleep 3 #wait for pg_ctl fork
  /usr/bin/psql -p 1115 -U postgres -f sql/create_pg_db.sql
  echo "Created postgres database."
fi

#sqlite3 database

if [ -d db/sqlite3_test.db ]; then
  echo "Not creating sqlite3 database. Already exists."
else
  sqlite3 db/sqlite3_test.db < sql/create_sqlite3_db.sql
  echo "Created sqlite3 database."
fi

popd > /dev/null
