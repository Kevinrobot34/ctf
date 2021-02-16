IMG            := ctf_env
CONTAINER_NAME := ctf_container

build:
		@docker build -t ${IMG} .

run:
		@docker run -it -v $(shell pwd):/src --rm \
			--cap-add=SYS_PTRACE --security-opt="seccomp=unconfined" \
			--name=${CONTAINER_NAME} ${IMG} /bin/bash
