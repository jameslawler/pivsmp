#!/bin/bash
source ./slowmovie/config/settings.cfg

SCRIPT=$( basename "$0" )
VERSION="1.0.0"
PIVSMP_SOURCE_PATH="./src"
PIVSMP_SCRIPT_PATH="./mock.sh"
PIVSMP_SCRIPT_PROCESS_NAME="mock.sh"
SLOWMOVIE_MOVIES_PATH="slowmovie/movies/"

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
  local PIVSMP_PID=$(pgrep -f $PIVSMP_SCRIPT_PROCESS_NAME)
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

  local PROGRESS_PERCENTAGE=$(( 100*10#$FRAME/10#$TOTAL_FRAMES ))
  local TIME_REMAINING_SECONDS=$(( (10#$TOTAL_FRAMES-10#$FRAME)*10#$DELAY ))
  local FORMATTED_TIME_REMAINING=$()
  local FORMATTED_END_DATE=$(date -d "+$TIME_REMAINING_SECONDS seconds")

  local txt=(
    "PiVSMP (Pi Very Slow Movie Player)"
    "Version: $VERSION"
    "-----------------------------"
    "Movie Status: $MOVIE_STATUS"
    "E-Ink Display: $DISPLAY_WIDTH * $DISPLAY_HEIGHT"
    "Raspberry Pi SPI: $SPI_STATUS"
    "-----------------------------"
    "Movie: $MOVIE"
    "Delay: $DELAY seconds"
    "-----------------------------"
    "Progress: $PROGRESS_PERCENTAGE%"
    "Current Frame: $FRAME"
    "Total Frames: $TOTAL_FRAMES"
    "Time Remaining: $TIME_REMAINING_SECONDS seconds ($FORMATTED_END_DATE)"
    "-----------------------------"
  )

  printf "%s\n" "${txt[@]}"
}

function choose-movie
{
  unset options i
  while IFS= read -r -d $'\0' f; do
    local MOVIE_NAME="${f/$SLOWMOVIE_MOVIES_PATH/''}"
    if [ ! -z "$MOVIE_NAME" ]
    then
      options[i++]="$MOVIE_NAME"
    fi
  done < <(find $SLOWMOVIE_MOVIES_PATH -type d -print0 )

  select opt in "${options[@]}"; do
    case $opt in
      "")
        echo "Please select a movie from the list"
      ;;
      *)
        CONFIGURE_MOVIE=$opt
        break
      ;;
    esac
  done
}

function choose-delay
{
  while :; do
    read -p "Delay (in seconds): " CONFIGURE_DELAY
    if ! [[ $CONFIGURE_DELAY =~ ^[0-9]+$ ]]
    then
      echo "Please enter a number"
      continue
    fi

    if (($CONFIGURE_DELAY >= 120))
    then
      break
    else
      echo "Please enter a number of at least 120 seconds"
    fi
  done
}

function app-configure
{
  python $PIVSMP_SOURCE_PATH/configure.py
  # echo "Choose a movie to show:"
  # choose-movie
  # echo "-----------------------------"
  # echo "How long do you want to wait between frames? (in seconds):"
  # choose-delay

  # local txt=(
  #   "Please confirm these new configurations"
  #   "Movie: $CONFIGURE_MOVIE"
  #   "Delay: $CONFIGURE_DELAY seconds"
  # )

  # printf "%s\n" "${txt[@]}"
}

function app-start
{
  $PIVSMP_SCRIPT_PATH > /dev/null &

  local PIVSMP_PID=$(pgrep -f $PIVSMP_SCRIPT_PROCESS_NAME)

  if [ -z "$PIVSMP_PID" ]
  then
    echo "Error: Unable to start Slow Movie"
  else
    echo "Slow Movie: Started"
    exit 1
  fi
}

function app-stop
{
  pkill -f $PIVSMP_SCRIPT_PROCESS_NAME > /dev/null
  local PIVSMP_PID=$(pgrep -f $PIVSMP_SCRIPT_PROCESS_NAME)

  if [ -z "$PIVSMP_PID" ]
  then
    echo "Slow Movie: Stopped"
  else
    echo "Error: Unable to stop Slow Movie"
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
  python $PIVSMP_SOURCE_PATH/clear.py
  echo "Display cleared"
}

function app-test
{
  app-stop
  python $PIVSMP_SOURCE_PATH/test.py
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

# nohup ./mock.sh > logs.txt 2>&1 &