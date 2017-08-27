from hashlib import sha256

from postgresql_handler import PostgreSQLHandler
from sqlite3_handler import SQLite3Handler

from . import POSTGRESQL
from . import SQLITE3

class DatabaseController(object):
  def __init__(self, databases, count):
    self.databases = databases
    self.count = count

    self.handlers = []

    for database in self.databases:
      if database == POSTGRESQL:
        handler = PostgreSQLHandler()

      elif database == SQLITE3:
        handler = SQLite3Handler()

      self.handlers.append(handler)

  def connect(self):
    [handler.connect() for handler in self.handlers]

  def insert(self):
    data = []
    for i in xrange(self.count):
      m = sha256(str(i)).hexdigest()
      data.append((i, m))

    [handler.insert(data) for handler in self.handlers]

  def read(self):
    [handler.read() for handler in self.handlers]

  def delete(self):
    [handler.delete() for handler in self.handlers]

  def close(self):
    [handler.close() for handler in self.handlers]

  def report(self):
    print 'Times in seconds'
    [handler.report() for handler in self.handlers]
