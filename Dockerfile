FROM parrotsec/core

RUN dpkg --add-architecture i386 && apt-get update && apt-get upgrade -y

# basic tools
RUN apt-get install -y --no-install-recommends \
  git man file curl wget vim \
  gdb ltrace strace \
  netcat nmap dnsutils \
  exiftool

# dev tools
RUN apt-get install -y --no-install-recommends \
  build-essential libssl-dev libffi-dev libreadline-dev zlib1g-dev hexedit

# x64環境でx86バイナリを動かすパッケージ
RUN apt-get install -y  --no-install-recommends \
  libc6:i386 libncurses5:i386 libstdc++6:i386 \
  gcc-multilib g++-multilib

# install python3
RUN apt-get install -y python3 python3-pip python3-dev \
  && python3 -m pip install --no-cache-dir --upgrade pip \
  && python3 -m pip install --no-cache-dir pwntools

# set up gdb-peda
RUN git clone https://github.com/longld/peda.git ~/peda \
  && echo "source ~/peda/peda.py" >> ~/.gdbinit

WORKDIR /src
