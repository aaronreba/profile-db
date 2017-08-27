from report_timer import ReportTimer

class DatabaseHandler(object):
  '''
  DatabaseHandler is an abstract class which provides base methods
  which can be overloaded by subclass specific database handlers.
  This class defines the primary report variables and functions.
  '''

  def __init__(self):
    '''
    Constructor. Will create timers.
    '''

    self.timers = {}

    self.timers = {}
    self.timers['insert'] = ReportTimer()
    self.timers['read'] = ReportTimer()
    self.timers['delete'] = ReportTimer()

  def connect(self):
    '''
    Defines connection to database. Subclass must implement.
    '''
    raise NotImplementedError()

  def insert(self):
    '''
    Defines insert to database. Subclass must implement.
    '''
    raise NotImplementedError()

  def read(self):
    '''
    Defines read from database. Subclass must implement.
    '''
    raise NotImplementedError()

  def delete(self):
    '''
    Defines delete from database. Subclass must implement.
    '''
    raise NotImplementedError()

  def close(self):
    '''
    Defines close from database. DBAPI defines all connections to have
    a close method which can simply be called here.
    '''
    self.connection.close()

  def report(self):
    '''
    Generate report text of handler. Displays mean and median for
    3 different tasks: insert, read, delete.
    '''
    print '{:10}: {}'.format('Database', self.database_name)

    task_prefix = '{task:10}:'
    formatted_result = '{field:>10}: {result:<20f}'

    for task in self.timers:
      timer = self.timers[task]

      mean = sum(timer.times) / float(len(timer.times))
      median = sorted(timer.times)[len(timer.times) / 2]

      result_line = ' '.join([
          task_prefix.format(task=task),
          formatted_result.format(field='Mean', result=mean),
          formatted_result.format(field='Median', result=median)
        ])
      print result_line

