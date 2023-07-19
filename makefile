.PHONY: init, run
init:
	pip3 install -r "requirements.txt"
run:
	time python3 etl.py