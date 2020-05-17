'''
	Optimize video generation by FFmpeg filters
	FFmpeg ref
		https://ffmpeg.org/ffmpeg-filters.html#concat
		https://ffmpeg.org/ffmpeg-filters.html#split_002c-asplit
		https://ffmpeg.org/ffmpeg-filters.html#movie-1
		https://ffmpeg.org/ffmpeg-filters.html#trim
		https://trac.ffmpeg.org/wiki/Creating%20multiple%20outputs
		https://superuser.com/questions/1212023/ffmpeg-settings-for-converting
		https://stackoverflow.com/questions/44510765/gpu-accelerated-video
			https://trac.ffmpeg.org/wiki/HWAccelIntro
		https://stackoverflow.com/questions/55687189/how-to-use-gpu-to
			May be able to use GPU for filters? 
	Sample
		$ ffmpeg -y -filter_complex '
			movie=png-0.png, scale=640:-1, loop=loop=-1:size=1:start=0, 
							trim=duration=0.5 [v1];
			movie=png-1.png, scale=640:-1, loop=loop=-1:size=1:start=0, 
							trim=duration=0.5 [v2];
			[v1] [v2] concat [out]; 
			[out] split [out1] [tmp]; 
			[tmp] subtitles=20200520Presentation.ass [out2]
			' -map '[out1]' a.mp4 -map '[out2]' b.mp4
'''

import os, sys, re
from subprocess import check_call

from slides import (FILE, MP3_FILE, START, OUT_DIR, ORI_PDF, OUT_FILE, SUB_FILE,
					OUT_SUB_FILE, get_dt)

if __name__ == '__main__' :
	dt = get_dt()
	N = len(dt)
	
	codec = 'libx264'
	if '--h264_nvenc' in sys.argv[1:] :
		codec = 'h264_nvenc'
	
	# ffmpeg
	print('ffmpeg')
	filter_graph = ''
	for index, i in enumerate(dt) :
		filter_graph += ('movie=png-%d.png, ' # scale=640:-1, 
						'loop=loop=-1:size=1:start=0, '
						'trim=duration=%f [v%d];\n' % 
						(index, i, index))
	for i in range(N) :
		filter_graph += '[v%d] ' % i
	filter_graph += '''	concat=n=%d [out]; 
						[out] split [out1] [tmp]; 
						[tmp] subtitles=20200520Presentation.ass [out2]
					''' % N
	conf = ['-max_muxing_queue_size', '4096', '-c:v', codec, 
			'-tune', 'stillimage', 
			'-profile:v', 'main', '-pix_fmt', 'yuv420p', '-c:a', 'copy']
	check_call(['ffmpeg', '-i', MP3_FILE, '-i', MP3_FILE, 
				'-filter_complex', filter_graph, 
				'-map', '[out1]', '-map', '0:a', *conf, 
				os.path.basename(OUT_FILE), 
				'-map', '[out2]', '-map', '1:a', *conf, 
				os.path.basename(OUT_SUB_FILE)], 
				cwd=OUT_DIR)

	print(ORI_PDF)
	print(OUT_FILE)
	print(SUB_FILE)
	print(OUT_SUB_FILE)
	# Rendering takes 43 min clock time, 81 min user time

