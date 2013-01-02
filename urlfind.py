import re
import sys

from optparse import OptionParser

if __name__ == "__main__":
	parser = OptionParser()
	parser.add_option('-i', dest='interactive', default=False,
			action='store_true', help='interactive mode')
	(options, args) = parser.parse_args()
	possible_urls = []
	for line in sys.stdin.readlines():
		urls = re.findall(r'https?://\S+', line)
		if urls:
			possible_urls.extend(urls)
		
	for count, url in enumerate(possible_urls):
		if options.interactive:
			print "%d) %s" % (count, url)
		else:
			print "%s" % url

