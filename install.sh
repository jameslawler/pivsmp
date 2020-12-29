#!/usr/bin/env bash

while true; do
  read -p "Do you wish to install Pi VSMP (Very Slow Movie Player)?" yn
  case $yn in
    [Yy]* ) echo "Yes";;
    [Nn]* ) exit;;
    * ) echo "Please answer yes or no.";;
  esac
done

# Confirm user wants to install
# apt-get update
# 
# Ask if the user wants to upgrade
# apt-get upgrade
#
# Ask the user which display they have
# Store for usage
#
# Install packages
# Enable SPI
# 
# Explain the `pivsmp` command