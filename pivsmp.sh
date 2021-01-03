#!/bin/bash

SCRIPT=$( basename "$0" )
VERSION="1.0.0"
PIVSMP_PROGRAM_PATH="/usr/local/pivsmp"
PIVSMP_PROCESS_NAME="pivsmp.py"

function usage
{
  local txt=(
    "PiVSMP (Pi Very Slow Movie Player)"
    "Version: $VERSION"
    ""
    "Usage: $SCRIPT [options] <command> [arguments]"
    ""
    "Commands:"
    "  status           See current status of the PiVSMP"
    "  configure        Configure player settings (movie, delay, position)"
    "  start            Start the current movie"
    "  stop             Stop the current movie (last frame stays)"
    "  restart          Restart the current movie (from the first frame)"
    "  clear            Clear the display"
    "  test             Runs the example display from Waveshare"
    ""
    "Options:"
    "  --help, -h       Print help"
    "  --version, -v    Print version"
  )

  printf "%s\n" "${txt[@]}"
}

function version
{
  local txt=(
    "$SCRIPT version $VERSION"
  )

  printf "%s\n" "${txt[@]}"
}

function app-status
{
  local PIVSMP_PID=$(pgrep -f $PIVSMP_PROCESS_NAME)
  local RASPI_CONFIG_SPI=$(raspi-config nonint get_spi)

  if [ -z "$PIVSMP_PID" ]
  then
    local MOVIE_STATUS="Stopped"
  else
    local MOVIE_STATUS="Running"
  fi

  if [ "$RASPI_CONFIG_SPI" == "0" ]
  then
    local SPI_STATUS="Enabled"
  else
    local SPI_STATUS="Disabled"
  fi

  local txt=(
    "PiVSMP (Pi Very Slow Movie Player)"
    "Version: $VERSION"
    "-----------------------------"
    "Movie Status: $MOVIE_STATUS"
    "Raspberry Pi SPI: $SPI_STATUS"
    "-----------------------------"
  )

  printf "%s\n" "${txt[@]}"
  python3 $PIVSMP_PROGRAM_PATH/status.py
}

function app-configure
{
  python3 $PIVSMP_PROGRAM_PATH/configure.py
}

function app-start
{
  nohup python3 $PIVSMP_PROGRAM_PATH/$PIVSMP_PROCESS_NAME > /dev/null &

  local PIVSMP_PID=$(pgrep -f $PIVSMP_PROCESS_NAME)

  if [ -z "$PIVSMP_PID" ]
  then
    echo "Error: Unable to start movie"
  else
    echo "Movie: Started"
    exit 1
  fi
}

function app-stop
{
  pkill -f $PIVSMP_PROCESS_NAME > /dev/null
  local PIVSMP_PID=$(pgrep -f $PIVSMP_PROCESS_NAME)

  if [ -z "$PIVSMP_PID" ]
  then
    echo "Movie: Stopped"
  else
    echo "Error: Unable to stop movie"
    exit 1
  fi
}

function app-restart
{
  app-stop
  app-start
}

function app-clear
{
  app-stop
  python3 $PIVSMP_PROGRAM_PATH/clear.py
  echo "Display cleared"
}

function app-test
{
  app-stop
  python3 $PIVSMP_PROGRAM_PATH/test.py
  echo "Check your display to see if there is a test message"
}

function badUsage
{
  local message="$1"
  local txt=(
    "Unrecognized parameters, to see possible commands execute:"
    "$SCRIPT --help"
  )

  [[ $message ]] && printf "$message\n"

  printf "%s\n" "${txt[@]}"
}

# Main function
while (( $# ))
do
  case "$1" in
    --help | -h)
      usage
      exit 0
    ;;

    --version | -v)
      version
      exit 0
    ;;

    status          \
    | configure     \
    | start         \
    | stop          \
    | restart       \
    | test          \
    | clear )
      command=$1
      shift
      app-$command $*
      exit 0
    ;;

    * )
      badUsage
      exit 1
    ;;
  esac
done

usage
exit 0