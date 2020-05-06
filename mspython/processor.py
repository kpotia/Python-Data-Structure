def process_numbers(mlist):
	rlist = []
	for i in mlist:
		if isnumeric(i):
			rlist.append(i)


	else: return rlist


def process_names(mlist):
	rlist = []
	for i in mlist:
		if not isnumeric(i):
			rlist.append(i)


	else: return rlist
