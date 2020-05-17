#!/bin/bash

OUT_DIR=/tmp/20200520Presentation
TC=$OUT_DIR/20200520transcript.txt
ORI_PDF=/tmp/20200520Presentation.pdf
OUT_FILE=$OUT_DIR/20200520Presentation.mp4
# DENSITY=52
DENSITY=154

rm -rf $OUT_DIR
mkdir -p $OUT_DIR

# Espeak
grep 'Transcript:' 20200520Presentation.tex | grep -oE ':.+' | cut -b 3- > $TC

i=0
while read p; do
	((i=$i+1))
	echo $i $(echo "$p" | cut -b -75)
	echo "$p" | espeak -w $OUT_DIR/$i.wav -z -s 130
done < $TC

N=`ls $OUT_DIR/*.wav | wc -l`

# Images
# gs -sDEVICE=pdfwrite -dSAFER -dNOPAUSE -dBATCH -o $OUT_DIR/%d.pdf $ORI_PDF
# pdftoppm $ORI_PDF $OUT_DIR/png -png
echo "convert: "
for i in `seq $N`; do
	((j=$i-1))
	echo -n "$i "
	convert -density $DENSITY "$ORI_PDF[$j]" -quality 90 "$OUT_DIR/$i.png"
done

# Videos
# https://superuser.com/questions/1041816/combine-one-image-one-audio-file-to-
pushd $OUT_DIR
echo "ffmpeg: "
for i in `seq $N`; do
	echo -n "$i "
	ffmpeg -hide_banner -i $i.png -i $i.wav $i.mp4 2> /dev/null
done
popd

# Final video
pushd $OUT_DIR
echo "concat: "
ffmpeg -safe 0 -f concat \
	-i <(for i in `seq $N`; do echo "file '$OUT_DIR/$i.mp4'"; done) \
	-max_muxing_queue_size 4096 -c:v libx264 -profile:v main -pix_fmt yuv420p \
	$OUT_FILE
popd

echo $TC
echo $OUT_FILE
echo ln $ORI_PDF $OUT_DIR

