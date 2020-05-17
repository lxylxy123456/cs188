from slides import OUT_DIR, ORI_PDF, get_dt
from subprocess import check_call

if not 'test' :
	DENSITY = 52
	CROP = []
else :
	DENSITY = 1219.2
	CROP = ['-resize', '1920x1080']

if __name__ == '__main__' :
	N = len(get_dt())
	for i in range(N):
		print(i, end=' ', flush=True)
		check_call([
			'convert', '-density', str(DENSITY), ORI_PDF + '[%d]' % i,
			'-quality', '90'] + CROP + [OUT_DIR + '/png-%d.png' % i])

