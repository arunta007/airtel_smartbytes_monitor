from matplotlib import pyplot as pl
from dateutil import parser
import calendar
import numpy as np
import csv
import sys

'''
The 'fname' sent to this module should be the name of a file which
has comma separated values in the format: MM-DD-YYYY, value
E.g:

12-10-2014, 5
12-11-2014, 11
12-12-2014, 14
12-13-2014, 19
12-14-2014, 23

The 'value' is nothing but the GiB used until that date.

Access this module as given below:

plotgraph(<filename>)

'''

#This function accepts file name and return two vectors containing date and value separately.
def getdata(fname):
	f = open(fname, 'rt')
	x = []
	y = []
	try:
		reader = csv.reader(f)
		for row in reader:
			x.append(row[:1])
			y.append(row[1:])
	finally:
		f.close()
	return x, y


#To strip day from date. Used for plotting the X-axis
def get_my(date):
	date_object = parser.parse(date)
	return date_object.month, date_object.year

#To strip month and year. Used for giving title to the graph
def getdateonly(dates):
	date_stripped = []
	for date in dates:
			
		date_object = parser.parse(date[0])
		date_stripped.append(str(date_object.day))
	return date_stripped

#Core method of this module. Accepts the file name of a csv as input and draws graph.
def plotgraph(fname):
	x_ticks, y = getdata(fname)
	x_ticks = getdateonly(x_ticks)
	l = len(x_ticks)
	x = np.array(range(1, l+1))
	pl.xticks(x, x_ticks)
	pl.plot(x, y, color = 'green', marker = 'o', linestyle = 'solid')
	m, y = get_my(x_ticks[0][0])
	month = calendar.month_name[int(m)]
	title = 'Airtel Internet: Usage Statistics for '+month+' '+str(y)
	pl.title (title)
	pl.ylabel("GiB Used So Far This Month")
	pl.xlabel("Date")
	pl.show()


#Testing:
#if __name__ == '__main__':
#	plotgraph('samplefile.csv')
