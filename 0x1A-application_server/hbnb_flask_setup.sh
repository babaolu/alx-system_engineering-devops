#!/usr/bin/bash

sudo apt update
sudo apt -y upgrade

sudo apt install -y net-tools build-essential pkg-config python3 python3-dev python3-pip default-libmysqlclient-dev zliblg-dev

pip3 install Flask gunicorn SQLAlchemy

MYSQLCLIENT_CFLAGS="-I/usr/include/mysql" MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient" pip3 install mysqlclient

sudo ufw allow in 5000/tcp
sudo ufw allow in 5001/tcp
sudo ufw allow in 5002/tcp

sudo ufw --force reload
git clone https://github.com/babaolu/AirBnB_clone_v2.git
git clone https://github.com/babaolu/AirBnB_clone_v3.git
