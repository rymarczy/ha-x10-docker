FROM debian:10

RUN apt-get update && apt-get upgrade -y

RUN apt-get install gcc make gawk libusb-1.0-0-dev wget -y

WORKDIR /root/mochad
RUN wget https://sourceforge.net/projects/mochad/files/mochad-0.1.17.tar.gz
RUN tar -xvf mochad-0.1.17.tar.gz

WORKDIR /root/mochad/mochad-0.1.17
RUN ./configure
RUN make
RUN make install
