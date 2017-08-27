from database_controller import DatabaseController

def profile(databases, count, iterations):
  '''
  Main method of profiling.

  Will perform n iterations of all tasks specified on all databases specified.
  '''

  database_controller = DatabaseController(databases, count)

  database_controller.connect()

  for i in xrange(iterations):
    database_controller.insert()
    database_controller.read()
    database_controller.delete()

  database_controller.close()

  database_controller.report()
