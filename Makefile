install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	#format code

lint:
	#flake8 or pylint

test:
	#some tests

build:
	#build container

run:
	#run docker

deploy:
	#deploy

all: install lint test deploy