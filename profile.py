#!/usr/bin/python

activate_this = 'pyenv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from profiler.arguments import ProfilerParser
from profiler.perform import profile

def main():
  ''' main() for profiler. Parses arguments and calls primary function'''

  parser = ProfilerParser()

  args = parser.parse_args()

  databases = args.databases
  count = args.count
  iterations = args.iterations

  profile(databases, count, iterations)

if __name__ == '__main__':
  main()
