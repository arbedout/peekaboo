NAME=peekaboo
RELEASE=$(shell git rev-parse --verify --short HEAD)
#RELEASE=$(shell date +'%Y%m%d%H%M%S')
INT_PORT=5050
EXT_PORT=5050

all:	build

clean:
	docker stop ${NAME} &>/dev/null || true
	docker rm ${NAME} &>/dev/null || true
	rm -rf build/ dist/ *.egg-info/

build:
	docker build --no-cache --rm=true -t ${NAME}:${RELEASE} .
	docker tag -f ${NAME}:${RELEASE} ${NAME}:latest

run: clean build
	docker run -d -p ${INT_PORT}:${EXT_PORT} --name=${NAME} ${NAME}:latest

stop:
	docker stop ${NAME}
	docker rm ${NAME}

publish:
	python setup.py sdist register upload
