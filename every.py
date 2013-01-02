#!/usr/bin/python
import sys

from optparse import OptionParser


if __name__ == "__main__":
	parser = OptionParser()
	parser.add_option('-n', help='number of lines to skip each time.',
		dest='lines', default=5)
	(options, args) = parser.parse_args()
	
	lines = long(options.lines)

	for i, line in enumerate(sys.stdin.readlines()):
		if i % lines == 0:
			sys.stdout.write(line)
