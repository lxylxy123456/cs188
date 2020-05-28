## Eric Li's ECS 188 Term Paper

### Presentation

Generate presentation video:

`make build/20200520Presentation.mp4`

If you have GPU, you can accelerate video encoding:

`make build/20200520Presentation.mp4 ARGS=--h264_nvenc`

### Final draft

Generate final draft of the paper:

`make build/20200526TermPaper.pdf`

### License

Unless otherwise specified, the content of this repo is licensed under
[https://creativecommons.org/licenses/by-nc-sa/4.0/](https://creativecommons.org/licenses/by-nc-sa/4.0/)

### Project structure

#### Source files
* `20200520Presentation.tex`: presentation slides source code
* `20200526TermPaper.pdf`: final draft source code
* `p2p.bib`: list of references
* `20200508_2244.mp3`: Audio file
* `20200508_2244.txt`: Transcript, without time info
* `20200508_2244.info`: Time info for transcript
* `20200508_2244.html`: HTML Player for `20200508_2244.*`
  (will display video after building `build/20200520Presentation.mp4`)

#### Build targets
* `build/20200520Presentation.pdf`: slides in pdf
* `build/png-0.png`: png files for each slide
* `build/20200520Presentation.ass`: subtitle file
* `build/20200520Presentation.mp4`: sresentation video
	* `build/20200520Presentation_sub.mp4`: subtitle drew on video
* `build/20200526TermPaper.pdf`: final draft in pdf
* `clean`: remove `./build/`

