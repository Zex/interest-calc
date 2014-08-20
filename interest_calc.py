#!/usr/bin/env python
#
# interest_calc.py
# Author: Zex <top_zlynch@yahoo.com>
#

import sys

interest_list = (0, 3.3, 4.13, 4.675, 0, 5.225)
#interest_list = (0, 3.3, 4.13, 4.25, 0, 4.75)

def profile_calc(principal, y, interest_index):

	if y == 0:
		return round((1+interest_index*interest_list[interest_index]/100)*principal, 2)
	elif y / interest_index < 2:
		return round(profile_calc(principal, y-interest_index, interest_index), 2)
	else:
		return round(profile_calc(principal, y-interest_index, interest_index)*(1+interest_index*interest_list[interest_index]/100), 2)


def interest_1235(argv):	

	if len(argv) < 4:
		print "money for 1, 2, 3 and 5-year"
		return
	
	prof_list = []
	
	prof_list.append(profile_calc(int(argv[0]), 6, 1))
	prof_list.append(profile_calc(int(argv[1]), 6, 2))
	prof_list.append(profile_calc(int(argv[2]), 6, 3))
	prof_list.append(profile_calc(int(argv[3]), 5, 5))
	
	return sum(prof_list)

if __name__ == "__main__":

	argvv = []
	
	try:
		cmb_fd = open("combinations")
		for line in cmb_fd:
			if len(line) < 4: continue
			if line[0] == '#': continue
			argvv.append(tuple(map(lambda x : int(x), line.split('\n')[0].split('|'))))
	
	except Exception as e:
		print e
		sys.exit()
	
	finally:
		print "close combinations"
		cmb_fd.close()
	
	try:
	
		ret = []
		for argv in argvv: 
			ret.append((interest_1235(argv), argv))
		
		ret.sort()
		print "ratio    %0.2f, %0.2f, %0.2f, %0.2f" % (interest_list[1], interest_list[2], interest_list[3], interest_list[5])
		print "sum     ", "(1-year, 2-year, 3-year, 5-year)"
		for r in ret:
			print r[0], r[1]
		
	except Exception as e:
		print e
	
	finally:
		sys.exit()







