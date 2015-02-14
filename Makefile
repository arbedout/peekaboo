NAME=peekaboo
#RELEASE=$(shell git rev-parse --verify --short HEAD)
RELEASE=$(shell date +'%Y%m%d%H%M%S')

all:	build

clean:
	docker stop peekaboo &>/dev/null || true
	docker rm peekaboo &>/dev/null || true

build:
	docker build -t ${NAME}:${RELEASE} .
	docker tag -f ${NAME}:${RELEASE} ${NAME}:latest

run: clean
	docker run -d -p 5000:5000 --name=peekaboo peekaboo:latest

stop:
	docker stop peekaboo
	docker rm peekaboo
