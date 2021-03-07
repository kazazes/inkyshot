FROM balenalib/raspberry-pi-python:3.7
# RUN ["cross-build-start"]

RUN install_packages \
  imagemagick wiringpi libjpeg-dev

COPY pip.conf /etc/pip.conf
RUN pip3 install spidev RPi.GPIO Pillow==8.1.1

COPY app /usr/app
WORKDIR /usr/app

ENV PYTHONPATH /usr/app/lib:$PYTHONPATH

CMD [ "/usr/app/entrypoint.sh" ]
