from time import time

class TimerErrror(Exception):
  pass

class ReportTimer(object):
  def __init__(self):
    self.timing = False
    self.times = []

  def start_timer(self):
    if self.timing:
      raise TimerError('Timing is already active')

    self.timing = True
    self.start_time = time()

  def end_timer(self):
    if not self.timing:
      raise TimerError('Timing is not active')

    end_time = time()
    self.timing = False
    time_taken = end_time - self.start_time

    self.times.append(time_taken)
