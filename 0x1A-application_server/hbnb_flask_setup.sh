#!/usr/bin/bash

sudo apt update
sudo apt -y upgrade
sudo apt install -y net-tools python3 python3-dev python3-pip
pip3 install Flask gunicorn
sudo ufw allow in 5000
sudo ufw --force reload
