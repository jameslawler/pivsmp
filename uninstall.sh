#!/usr/bin/env bash

function remove-installation-repository
{
  echo "(starting)    removing pivsmp repository in /tmp if exists"
  sudo rm -rf /tmp/pivsmp
  echo "(complete)    removing pivsmp repository in /tmp if exists"
}

function remove-pivsmp-program
{
  echo "(starting)    removing pivsmp program"
  sudo rm -rf /usr/local/pivsmp
  sudo rm -f /usr/local/bin/pivsmp
  echo "(complete)    removing pivsmp program"
}

function remove-home-folders
{
  echo "(starting)    removing home folders (~/.pivsmp)"
  rm -rf ~/.pivsmp
  echo "(complete)    removing home folders (~/.pivsmp)"
}

function main
{
  while true; do
    read -p "Do you wish to uninstall Pi VSMP (Very Slow Movie Player)? [y/n]: " yn
    case $yn in
      [Yy]* )
        remove-installation-repository
        remove-pivsmp-program
        break
      ;;
      [Nn]* )
        echo "Uninstall aborted."
        exit
      ;;
      * )
        echo "Please answer yes or no."
      ;;
    esac
  done

  while true; do
    read -p "Do you wish to remove home folders (~/.pivsmp)? This will remove any movies in the movies folder and your pivsmp configuration [y/n]: " yn
    case $yn in
      [Yy]* )
        remove-home-folders
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

  echo "------------------------"
  echo " Uninstall Complete! "
  echo "------------------------"
  echo ""
  echo " Note: This script has not removed any installed packages."
  echo " It has only removed PiVSMP and its folders"
  echo ""
  echo " Thank you for using PiVSMP."
  echo ""
}

main "$@"
