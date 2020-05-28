BUILD_DIR=./build

build/20200526TermPaper.pdf: 20200526TermPaper.tex p2p.bib
	mkdir -p $(BUILD_DIR)
	pdflatex -output-directory $(BUILD_DIR) 20200526TermPaper.tex
	cp p2p.bib $(BUILD_DIR)
	cd $(BUILD_DIR); bibtex 20200526TermPaper.aux
	pdflatex -output-directory $(BUILD_DIR) 20200526TermPaper.tex
	pdflatex -output-directory $(BUILD_DIR) 20200526TermPaper.tex

build/20200520Presentation.pdf: 20200520Presentation.tex p2p.bib
	mkdir -p $(BUILD_DIR)
	pdflatex -output-directory $(BUILD_DIR) 20200520Presentation.tex
	cp p2p.bib $(BUILD_DIR)
	cd $(BUILD_DIR); bibtex 20200520Presentation.aux
	pdflatex -output-directory $(BUILD_DIR) 20200520Presentation.tex
	pdflatex -output-directory $(BUILD_DIR) 20200520Presentation.tex

build/20200520Presentation.ass: ass.py 20200508_2244.txt 20200508_2244.info
	mkdir -p $(BUILD_DIR)
	python3 ass.py

build/png-0.png: convert.py build/20200520Presentation.pdf
	python3 convert.py

build/20200520Presentation.mp4: build/png-0.png build/20200520Presentation.ass \
	filter.py 20200508_2244.mp3
	ln -sf "$(PWD)"/20200508_2244.mp3 $(BUILD_DIR)
	python3 filter.py $(ARGS)

clean:
	rm -rf $(BUILD_DIR)
