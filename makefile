all: panitan cherry
.PHONY: all

cherry:
	python main.py 1979 11 2
.PHONY: cherry

panitan:
	python main.py 1985 9 27
.PHONY: panitan

format:
	yapf -i *.py
.PHONY: format

clean:
	rm -rf *.pyc *.png
.PHONY: clean

