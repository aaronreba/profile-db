from database_handler import DatabaseHandler

def profile(databases, count, iterations):
  '''
  Main method of profiling.

  Will perform n iterations of all tasks specified on all databases specified.
  '''

  database_handler = DatabaseHandler(databases, count)

  database_handler.connect()

  for i in xrange(iterations):
    database_handler.insert()
    database_handler.read()
    database_handler.delete()

  database_handler.close()

  database_handler.report()
