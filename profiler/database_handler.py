from report_timer import ReportTimer

class DatabaseHandler(object):
  def __init__(self):
    self.timers = {}

    self.timers = {}
    self.timers['insert'] = ReportTimer()
    self.timers['read'] = ReportTimer()
    self.timers['delete'] = ReportTimer()

  def connect(self):
    raise NotImplementedError()


  def insert(self):
    raise NotImplementedError()

  def read(self):
    raise NotImplementedError()

  def delete(self):
    raise NotImplementedError()

  def close(self):
    self.connection.close()

  def report(self):
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

