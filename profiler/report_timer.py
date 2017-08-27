from time import time

class TimerErrror(Exception):
  '''
  Simple exception used by ReportTimer to throw exceptions related to
  timer start and stops
  '''
  pass

class ReportTimer(object):
  '''
  ReportTimer is a timer that will track durations
  in between when start_timer() and end_timer() are called. 
  '''
  def __init__(self):
    '''
    Constructor. Sets empty timer information.
    '''
    self.timing = False
    self.times = []

  def start_timer(self):
    '''
    Starts timing.
    '''
    if self.timing:
      raise TimerError('Timing is already active')

    self.timing = True
    self.start_time = time()

  def end_timer(self):
    '''
    Stops timing. Appends duration to self.times
    '''
    if not self.timing:
      raise TimerError('Timing is not active')

    end_time = time()
    self.timing = False
    time_taken = end_time - self.start_time

    self.times.append(time_taken)
