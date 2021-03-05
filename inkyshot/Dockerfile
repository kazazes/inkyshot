FROM balenalib/raspberry-pi-debian-python:3.7-buster

# RUN ["cross-build-start"]

RUN install_packages \
  imagemagick \
  unzip \
  wiringpi \
  p7zip-full \
  wget 

RUN install_packages \
  python3-dev python3-setuptools python3-wheel python3-pip python3-pil

RUN mkdir -p /tmp/sdk && \
  cd /tmp/sdk && \
  wget http://www.waveshare.net/w/upload/9/9a/12.48inch_e-Paper_Module_Code_RPI.7z && \
  7z x 12.48inch_e-Paper_Module_Code_RPI.7z  -r -o./waveshare-sdk && \
  chmod 777 -R waveshare-sdk && \
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

# RUN ["cross-build-end"]

CMD [ "/usr/app/entrypoint.sh" ]
