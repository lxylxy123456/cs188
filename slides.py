'''
	Generate slides
'''

import os, sys, re
from subprocess import check_call

FILE = '20200508_2244'
MP3_FILE = FILE + '.mp3'
START = '#,'
OUT_DIR = './build'
ORI_PDF = './build/20200520Presentation.pdf'
OUT_FILE = OUT_DIR + '/20200520Presentation.mp4'
SUB_FILE = OUT_DIR + '/20200520Presentation.ass'
OUT_SUB_FILE = OUT_DIR + '/20200520Presentation_sub.mp4'

def get_dt() :
	a = open(FILE + '.txt').read().split('\n')
	while not a[-1] :
		a.pop()
	b = next(filter(lambda x: x.startswith(START), 
					open(FILE + '.info').read().split('\n')))
	c = b.split(',')
	while not c[-1] :
		c.pop()
	count = 0
	# collect times
	times = [0]
	for index, i in enumerate(a) :
		if not i :
			times.append((float(c[count * 2]) + float(c[count * 2 + 1])) / 2)
		else :
			count += 1
	times.append((float(c[count * 2]) + float(c[count * 2 + 1])) / 2)
	# compute dt
	dt = list(map(lambda x, y: x - y, times[1:], times[:-1]))
	
	return dt

