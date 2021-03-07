FROM balenalib/raspberry-pi-python:3.7
# RUN ["cross-build-start"]

RUN install_packages \
  imagemagick \
  wiringpi \
  libjpeg-dev

COPY pip.conf /etc/pip.conf
RUN pip3 install spidev RPi.GPIO Pillow==8.1.1

COPY app /usr/app
WORKDIR /usr/app

RUN install_packages gcc make libtool automake && \
  cd lib/bcm2835-1.68 && \
  ./configure && \
  make && \
  make install && \
  apt-get remove -yq gcc make libtool automake

CMD [ "/usr/app/entrypoint.sh" ]
