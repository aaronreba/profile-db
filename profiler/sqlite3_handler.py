import sqlite3

from . import SQLITE3
from . import SQLITE3_LOCATION

from database_handler import DatabaseHandler

class SQLite3Handler(DatabaseHandler):
  def __init__(self):
    super(self.__class__, self).__init__()
    self.database_name = SQLITE3

  def connect(self):
    self.connection = sqlite3.connect(
      SQLITE3_LOCATION
    )
    self.clean()

  def clean(self):
    cursor = self.connection.cursor()

    query = 'DELETE FROM main.sample_data;'
    cursor.execute(query)
    self.connection.commit()

    cursor.close()

  def insert(self, items):
    timer = self.timers['insert']

    cursor = self.connection.cursor()

    records_list_template = ', '.join(['(?, ?)'] * len(items))
    query = ('INSERT INTO main.sample_data (id, sha256) '
      'VALUES {}').format(records_list_template)

    query_args = []
    for entry in items:
      for subentry in entry:
        query_args.append(subentry)

    timer.start_timer()
    cursor.execute(query, query_args)
    timer.end_timer()

    self.connection.commit()

    cursor.close()

  def read(self):
    timer = self.timers['read']

    cursor = self.connection.cursor()

    query = 'SELECT * FROM main.sample_data;'

    timer.start_timer()
    cursor.execute(query)
    results = cursor.fetchall()
    timer.end_timer()

    cursor.close()

  def delete(self):
    timer = self.timers['delete']

    cursor = self.connection.cursor()

    query = 'DELETE FROM main.sample_data;'

    timer.start_timer()
    cursor.execute(query)
    timer.end_timer()

    self.connection.commit()

    cursor.close()

