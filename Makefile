IMG            := ctf_env
CONTAINER_NAME := ctf_container

build:
		@docker build -t ${IMG} .

run:
		@docker run -it -v $(shell pwd):/src --rm --name=${CONTAINER_NAME} ${IMG} /bin/bash
