all:
	python main.py 1985 9 27
.PHONY: all

format:
	yapf -i *.py
.PHONY: format

clean:
	rm -rf *.pyc *.png
.PHONY: clean

