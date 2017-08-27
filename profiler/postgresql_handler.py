import psycopg2

from . import POSTGRESQL
from . import POSTGRESQL_DB_NAME
from . import POSTGRESQL_USER
from . import POSTGRESQL_PASSWORD
from . import POSTGRESQL_HOST
from . import POSTGRESQL_PORT

from database_handler import DatabaseHandler

class PostgreSQLHandler(DatabaseHandler):
  '''
  Postgresql database handler. Defines specific methods for accessing
  the Postgresql database.
  '''
  def __init__(self):
    '''
    Constructor. Initializes magic string identity.
    '''
    super(self.__class__, self).__init__()
    self.database_name = POSTGRESQL

  def connect(self):
    '''
    Connects to Postgresql database.
    '''
    self.connection = psycopg2.connect(
      dbname=POSTGRESQL_DB_NAME,
      user=POSTGRESQL_USER,
      password=POSTGRESQL_PASSWORD,
      host=POSTGRESQL_HOST,
      port=POSTGRESQL_PORT,
    )
    self.clean()

  def clean(self):
    '''
    Cleans all data from database relevant for testing.
    '''
    cursor = self.connection.cursor()

    query = 'DELETE FROM data.sample_data;'
    cursor.execute(query)
    self.connection.commit()

    cursor.close()

  def insert(self, items):
    '''
    Creates insert query and inserts everything to database
    '''
    timer = self.timers['insert']

    cursor = self.connection.cursor()

    # psycopg2's executemany() does multiple insert statements rather than
    # creating a compound insert statement. Manually create
    # the compound insert statement here.
    records_list_template = ', '.join(['(%s, %s)'] * len(items))
    query = ('INSERT INTO data.sample_data (id, sha256) '
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
    '''
    Reads data from database and pulls data into Python space.
    Cursor's execute() and fetchall() are both timed.
    '''
    timer = self.timers['read']

    cursor = self.connection.cursor()

    query = 'SELECT * FROM data.sample_data;'

    timer.start_timer()
    cursor.execute(query)
    results = cursor.fetchall()
    timer.end_timer()

    cursor.close()

  def delete(self):
    '''
    Deletes data that was inserted.
    '''
    timer = self.timers['delete']

    cursor = self.connection.cursor()

    query = 'DELETE FROM data.sample_data;'

    timer.start_timer()
    cursor.execute(query)
    timer.end_timer()

    self.connection.commit()

    cursor.close()

