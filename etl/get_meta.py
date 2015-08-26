__author__ = 'Matias Estrada'

import sys


# id = {D10-1001}
# author = {Rush, Alexander M.; Sontag, David...}
# title = {On Dual Decomposition and Linear ...}
# venue = {EMNLP}
# year = {2010}
#

def get_meta(iter_parts, chunk=6):
	current = []
	counter = 0
	for part in iter_parts:
		current.append(map(lambda x: x.strip('{}'), part.strip().split(' = ')))
		counter += 1
		if counter % 6 == 0:
			current = filter(lambda x: len(x) > 1, current)
			yield current
			counter = 0
			current = []

def get_elem(field, iterobj):
	try:
		return filter(lambda x: x[0] == field, iterobj)[0][1]
	except Exception:
		print field
		print iterobj
		raise

for entry in get_meta(sys.stdin):
	
	try:
		pid = get_elem('id', entry)
		title = get_elem('title', entry)
		venue = get_elem('venue', entry)
		year = get_elem('year', entry)
	except Exception:
		print entry
		raise

	print "{0}\t{1}\t{2}\t{3}".format(pid, title, venue, year)
