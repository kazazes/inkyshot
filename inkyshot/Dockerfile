FROM balenalib/raspberry-pi-debian-python:3.7-buster

RUN ["cross-build-start"]

RUN pip3 install --upgrade pip wheel

RUN install_packages \
  imagemagick \
  unzip \
  wiringpi \
  p7zip-full \
  build-essential \
  wget

RUN pip3 install --upgrade RPi.GPIO spidev

RUN mkdir -p /tmp/bcm2835 && \
  cd /tmp/bcm2835 && \
  wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz && \
  tar zxvf bcm2835-1.60.tar.gz && \
  cd bcm2835-1.60/ && \
  ./configure && \
  make && \
  make install && \
  rm -rf /tmp/bcm2835

RUN mkdir -p /tmp/waveshare-sdk && \
  cd /tmp/waveshare-sdk && \
  wget http://www.waveshare.net/w/upload/9/9a/12.48inch_e-Paper_Module_Code_RPI.7z && \
  7z x 12.48inch_e-Paper_Module_Code_RPI.7z  -r -o./sdk && \
  chmod 777 -R sdk && \
  mv sdk /opt/waveshare-sdk && \
  cd /opt/waveshare-sdk && ls -al && \
  rm -rf /tmp/waveshare-sdk 

WORKDIR /usr/app

RUN wget https://github.com/louwrentius/waveshare-12.48inch-3-color-e-ink/archive/main.zip && \
  unzip main.zip && \
  mv waveshare-12.48inch-3-color-e-ink-main waveshare-display &&\
  rm -rf main.zip \
  && ls -al

COPY images images

RUN ["cross-build-end"]

CMD ["PYTHONPATH=/opt/waveshare-sdk/python/lib:${PYTHONPATH}","python3", "/usr/app/waveshare-display/display.py", "-i", "/usr/app/images/lords.jpg"]