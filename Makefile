# The usual

SHELL := /bin/bash

test:
	python t/test_basic.py

clean:
	rm -rf test-reports *.pyc
