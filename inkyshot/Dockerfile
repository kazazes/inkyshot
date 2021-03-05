FROM balenalib/raspberry-pi-python:3.7

RUN ["cross-build-start"]

RUN install_packages \
  imagemagick \
  unzip \
  wiringpi \
  p7zip-full \
  wget 

COPY pip.conf /etc/pip.conf
RUN pip3 install --upgrade pip spidev RPi.GPIO Pillow

RUN mkdir -p /tmp/sdk && cd /tmp/sdk && \
  wget http://www.waveshare.net/w/upload/9/9a/12.48inch_e-Paper_Module_Code_RPI.7z && \
  7z x 12.48inch_e-Paper_Module_Code_RPI.7z  -r -o./waveshare-sdk && \
  mv waveshare-sdk /opt/ && \
  cd /opt/waveshare-sdk && \
  rm -rf /tmp/sdk 

WORKDIR /usr/app

RUN wget https://github.com/louwrentius/waveshare-12.48inch-3-color-e-ink/archive/main.zip && \
  unzip main.zip && \
  mv waveshare-12.48inch-3-color-e-ink-main waveshare-display &&\
  rm -rf main.zip 

COPY images images
COPY entrypoint.sh entrypoint.sh

RUN ["cross-build-end"]

CMD [ "/usr/app/entrypoint.sh" ]
