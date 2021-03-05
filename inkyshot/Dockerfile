FROM balenalib/raspberry-pi-debian-python:3.7-buster-build

# RUN ["cross-build-start"]

RUN install_packages \
  imagemagick \
  unzip \
  wiringpi \
  p7zip-full

# RUN pip3 install RPi.GPIO spidev

RUN mkdir -p /tmp/waveshare-sdk && \
  cd /tmp/waveshare-sdk && \
  wget http://www.waveshare.net/w/upload/9/9a/12.48inch_e-Paper_Module_Code_RPI.7z && \
  7z x 12.48inch_e-Paper_Module_Code_RPI.7z  -r -o./sdk && \
  chmod 777 -R sdk && \
  mv sdk /opt/waveshare-sdk && \
  cd /opt/waveshare-sdk && \
  rm -rf /tmp/waveshare-sdk 

WORKDIR /usr/app

RUN wget https://github.com/louwrentius/waveshare-12.48inch-3-color-e-ink/archive/main.zip && \
  unzip main.zip && \
  mv waveshare-12.48inch-3-color-e-ink-main waveshare-display &&\
  rm -rf main.zip \
  && ls -al

COPY images images
COPY entrypoint.sh entrypoint.sh

# RUN ["cross-build-end"]

CMD [ "/usr/app/entrypoint.sh" ]
