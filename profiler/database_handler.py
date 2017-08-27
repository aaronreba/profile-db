from hashlib import sha256

import psycopg2
import sqlite3

from report_timer import ReportTimer

from . import POSTGRESQL
from . import POSTGRESQL_DB_NAME
from . import POSTGRESQL_USER
from . import POSTGRESQL_PASSWORD
from . import POSTGRESQL_HOST
from . import POSTGRESQL_PORT

from . import SQLITE3
from . import SQLITE3_LOCATION

class DatabaseHandler(object):
  def __init__(self, databases, count):
    self.databases = databases
    self.count = count

    self.connections = {}
    self.timers = {}

    for database in self.databases:
      self.timers[database] = {}
      self.timers[database]['insert'] = ReportTimer()
      self.timers[database]['read'] = ReportTimer()
      self.timers[database]['delete'] = ReportTimer()

  def connect(self):
    if POSTGRESQL in self.databases:
      self.connections[POSTGRESQL] = psycopg2.connect(
        dbname=POSTGRESQL_DB_NAME,
        user=POSTGRESQL_USER,
        password=POSTGRESQL_PASSWORD,
        host=POSTGRESQL_HOST,
        port=POSTGRESQL_PORT,
      )

    if SQLITE3 in self.databases:
      self.connections[SQLITE3] = sqlite3.connect(
        SQLITE3_LOCATION
      )

  def insert(self):
    # Create i count of sha256

    hashes = []

    for i in xrange(self.count):
      m = sha256(str(i)).hexdigest()
      hashes.append(m)

    for database in self.databases:
      timer = self.timers[database]['insert']

      connection = self.connections[database]
      cursor = connection.cursor()

      insert_data = [(i, h) for i, h in enumerate(hashes)]
      insert_string = 'INSERT INTO data.sample_data (id, sha256) VALUES (%s)'

      timer.start_timer()
      cursor.execute(insert_string, insert_data)
      timer.end_timer()

      cursor.close()

  def read(self):
    for database in self.databases:
      timer = self.timers[database]['read']

      connection = self.connections[database]
      cursor = connection.cursor()

      timer.start_timer()
      timer.end_timer()

      cursor.close()

  def delete(self):
    for database in self.databases:
      timer = self.timers[database]['delete']

      connection = self.connections[database]
      cursor = connection.cursor()

      timer.start_timer()
      timer.end_timer()

      cursor.close()

  def close(self):
    for database in self.databases:
      connection = self.connections[database]
      connection.close()

  def report(self):
    for database in self.databases:
      print database
      database_timers = self.timers[database]
      for task in database_timers:
        print task
        timer = database_timers[task]

        mean = sum(timer.times) / float(len(timer.times))
        print 'mean', mean
        median = sorted(timer.times)[len(timer.times) / 2]
        print 'median', median

