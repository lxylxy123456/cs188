'''
	Generate ass files
'''

import os, sys, re
from subprocess import check_call

from slides import FILE, START, OUT_DIR, SUB_FILE

def f2t(ts) :
	hms = int(ts)
	u = ts - hms
	hm, s = divmod(hms, 60)
	h, m = divmod(hm, 60)
	return '%d:%02d:%02d.%02d' % (h, m, s, int(u * 100))

if __name__ == '__main__' :
	a = open(FILE + '.txt').read().split('\n')
	while not a[-1] :
		a.pop()
	a = list(map(lambda x: re.sub('\([^\(\)]+\)', '', x), a))
	b = next(filter(lambda x: x.startswith(START), 
					open(FILE + '.info').read().split('\n')))
	c = list(map(float, b.split(',')[1:]))
	while not c[-1] :
		c.pop()
	count = 0
	c.pop()
	# collect times
	while '' in a :
		a.remove('')

	assert len(a) * 2 == len(c)

	c = list(map(lambda x: x - 0.5, c))

	# of = sys.stdout
	of = open(SUB_FILE, 'w')
	print('[Script Info]', file=of)
	print('Title:Eric Li P2P Presentation', file=of)
	print('Original Script:Eric Li', file=of)
	print('Collisions:Normal', file=of)
	print('PlayResX:704', file=of)
	print('PlayResY:396', file=of)
	print('Timer:100.0000', file=of)
	print('', file=of)
	print('[V4+ Styles]', file=of)
	print('Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, '
			'Outline, Alignment', file=of)
	print('Style: Default, Arial, 16, &H00888888, &H00FFFFFF, 1, 2', file=of)
	print('', file=of)
	print('[Events]', file=of)
	print('Format: Layer, Start, End, Style, Text', file=of)
	for index, i in enumerate(a) :
		print('Dialogue: 0,%s,%s,Default,%s' % 
				(f2t(c[2*index]), f2t(c[2*index+1]), i), file=of)
	print(SUB_FILE, file=sys.stderr)

