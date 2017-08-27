from hashlib import sha256

from postgresql_handler import PostgreSQLHandler
from sqlite3_handler import SQLite3Handler

from . import POSTGRESQL
from . import SQLITE3

class DatabaseController(object):
  '''
  DatabaseController will instantiate database handlers
  and create test data based on the databases and count parameters.

  DatabaseController provides methods for accessing database handlers.
  '''

  def __init__(self, databases, count):
    '''
    Constructor. Will create handlers.
    '''
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
    '''
    Calls all handlers connect() methods.
    '''
    [handler.connect() for handler in self.handlers]

  def insert(self):
    '''
    Creates data and calls all handlers insert() methods.
    '''

    data = []
    for i in xrange(self.count):
      m = sha256(str(i)).hexdigest()
      data.append((i, m))

    [handler.insert(data) for handler in self.handlers]

  def read(self):
    '''
    Calls all handlers read() methods.
    '''
    [handler.read() for handler in self.handlers]

  def delete(self):
    '''
    Calls all handlers delete() methods.
    '''
    [handler.delete() for handler in self.handlers]

  def close(self):
    '''
    Calls all handlers close() methods.
    '''
    [handler.close() for handler in self.handlers]

  def report(self):
    '''
    Calls all handlers report() methods.
    '''
    print 'Times in seconds'
    [handler.report() for handler in self.handlers]
