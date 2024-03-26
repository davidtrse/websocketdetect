setup:
	python3 -m venv . \
	a=$(pwd); \
	source "$a/bin/activate" \
	python3 -m pip install websockets
#❯ pip3 install websockets
init:
	pip3 install -r requirements.txt

run: 
	python3 main.py
.PHONY: setup init