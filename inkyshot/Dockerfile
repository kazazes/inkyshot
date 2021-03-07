FROM balenalib/raspberry-pi-alpine-python:3.7
RUN ["cross-build-start"]

RUN install_packages \
  imagemagick \
  wiringpi

COPY pip.conf /etc/pip.conf
RUN pip3 install spidev RPi.GPIO Pillow==8.1.1

COPY app /usr/app
WORKDIR /usr/app

CMD [ "/usr/app/entrypoint.sh" ]
