#!/usr/bin/env bash

function system-packages-update
{
  echo "(starting)    sudo apt-get update"
  #sudo apt-get update
  echo "(complete)    sudo apt-get update"
}

function system-packages-upgrade
{
  echo "(starting)    sudo apt-get upgrade"
  #sudo apt-get upgrade
  echo "(complete)    sudo apt-get upgrade"
}

function install-git
{
  echo "(starting)    sudo apt-get install git"
  sudo apt-get install -y git
  echo "(complete)    sudo apt-get install git"
}

function clone-installation-repository
{
  echo "(starting)    cloning pivsmp repository"
  sudo rm -r /tmp/pivsmp
  sudo git clone https://github.com/jameslawler/pivsmp.git /tmp/pivsmp
  echo "(complete)    cloning pivsmp repository"
}

function python-packages
{
  echo "(starting)    sudo apt-get install python3-pip python3-pil python3-numpy"
  sudo apt-get install -y python3-pip python3-pil python3-numpy
  echo "(complete)    sudo apt-get install python3-pip python3-pil python3-numpy"

  echo "(starting)    sudo pip3 install --no-cache-dir RPi.GPIO"
  sudo pip3 install --no-cache-dir RPi.GPIO
  echo "(complete)    sudo pip3 install --no-cache-dir RPi.GPIO"

  echo "(starting)    sudo pip3 install --no-cache-dir spidev"
  sudo pip3 install --no-cache-dir spidev
  echo "(complete)    sudo pip3 install --no-cache-dir spidev"

  echo "(starting)    sudo pip3 install --no-cache-dir questionary"
  sudo pip3 install --no-cache-dir questionary
  echo "(complete)    sudo pip3 install --no-cache-dir questionary"
}

function waveshare-driver
{
  echo "(starting)    installing waveshare driver"
  cd /tmp/pivsmp/waveshare-driver
  sudo python3 setup.py install
  echo "(complete)    installing waveshare driver"
}

function install-pivsmp-program
{
  echo "(starting)    installing pivsmp program"
  sudo mkdir -p /usr/local/pivsmp
  sudo cp /tmp/pivsmp/src/* /usr/local/pivsmp
  sudo cp /tmp/pivsmp/pivsmp.sh /usr/local/bin/pivsmp
  sudo chmod +x /usr/local/bin/pivsmp
  echo "(complete)    installing pivsmp program"
}

function create-folders
{
  echo "(starting)    creating folders (~/.pivsmp)"
  mkdir -p ~/.pivsmp
  mkdir -p ~/.pivsmp/config
  mkdir -p ~/.pivsmp/movies
  echo "(complete)    creating folders (~/.pivsmp)"
}

while true; do
  read -p "Do you wish to install Pi VSMP (Very Slow Movie Player)? [y/n]: " yn
  case $yn in
    [Yy]* )
      system-packages-update
      break
    ;;
    [Nn]* )
      exit
    ;;
    * )
      echo "Please answer yes or no."
    ;;
  esac
done

while true; do
  read -p "It is recommended to do a system update before installing. Would you like to? [y/n]: " yn
  case $yn in
    [Yy]* )
      system-packages-upgrade
      break
    ;;
    [Nn]* )
      break
    ;;
    * )
      echo "Please answer yes or no."
    ;;
  esac
done

install-git
clone-installation-repository
python-packages
waveshare-driver
install-pivsmp-program
create-folders

# Enable SPI
# 
# Explain the `pivsmp` command