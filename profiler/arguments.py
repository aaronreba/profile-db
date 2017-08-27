from argparse import ArgumentParser
from argparse import ArgumentTypeError

from . import AVAILABLE_DATABASES

def positive_integer(value):
  '''
  Method for validating argument. Checks to see if it's a positive integer.
  '''
  try:
    v = int(value)
  except Exception as e:
    raise ArgumentTypeError(str(e))

  if v < 1:
    raise ArgumentTypeError('Argument less than 1: {}'.format(value))

  return v

class ProfilerParser(ArgumentParser):
  def __init__(self, *args, **kwargs):
    description = '''Simple Python database module profiler

This will attempt to insert, read, and then delete a specified number
of rows from the specified databases.
'''

    super(self.__class__, self).__init__(*args,
      description=description, **kwargs)

    self.add_argument(
      '-d', '--databases',
      required=True,
      choices=AVAILABLE_DATABASES,
      action='append',
      help='Comma separated list of databases to perform tasks on. '
           'Will choose all databases as default.'
    )

    self.add_argument(
      '-c', '--count',
      type=positive_integer,
      required=True,
      help='Data set size to use'
    )

    self.add_argument(
      '-i', '--iterations',
      type=positive_integer,
      required=True,
      help='Number of iterations to perform for given task'
    )

