FROM balenalib/raspberry-pi-python:3.7
# RUN ["cross-build-start"]

COPY pip.conf /etc/pip.conf
RUN pip3 install spidev RPi.GPIO Pillow==8.1.1

COPY app/lib /usr/app/lib

RUN install_packages \
  # build deps
  gcc make libtool automake \ 
  # runtime deps
  imagemagick wiringpi libjpeg-dev && \ 
  cd /usr/app/lib/bcm2835-1.68 && \
  ./configure && \
  make && \
  make install && \
  apt-get remove -yq gcc make libtool automake && \
  rm -rf /usr/app/lib/bcm2835-1.68

COPY app /usr/app
WORKDIR /usr/app

CMD [ "/usr/app/entrypoint.sh" ]
