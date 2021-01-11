# Pi Very Slow Movie Player

## Installation

Method 1: Run straight from GitHub by using this command on your Pi

`bash <(curl -s https://raw.githubusercontent.com/jameslawler/pivsmp/main/install.sh)`

Method 2: Clone `https://github.com/jameslawler/pivsmp.git` and run `./install.sh`

### Changes

The following changes are made to your Pi during this installation.

1. `sudo apt-get update`
2. `sudo apt-get upgrade` (optional)
3. `sudo apt-get install git`
4. Remove contents of `/tmp/pivsmp` and clone a fresh copy of `https://github.com/jameslawler/pivsmp.git`
5. Install python packages

- `sudo apt-get install python3-pip python3-pil python3-numpy`
- `sudo pip3 install RPi.GPIO`
- `sudo pip3 install spidev`
- `sudo pip3 install questionary`

6. Install Waveshare driver
7. Install `pivsmp` python source to `/usr/local/pivsmp`
8. Install `pivsmp` shell script to `/usr/local/bin/pivsmp`
9. Create config and movie folders at `~/.pivsmp`
10. Enable SPI interface using `raspi-config`

## Usage

After installation you can configure, start, stop, and see the status of the `pivsmp` by running the command anywhere in a console of your pi.

Run `pivsmp` to see all commands provided by the program.

1. Copy a movie to your `~/.pivsmp/movies` folder. The movie must be inside a folder with the name of the movie. You can use a SFTP program on your main machine to copy the movie to the Pi.
2. In your Pi console run `pivsmp configure`.

- Select your e-paper display
- Select the movie to display
- Choose a frame to start on
- Choose a delay seconds between frames

3. Start the movie by running `pivsmp start`
4. Verify the status using `pivsmp status`

## Uninstallation

To remove the folders and pivsmp program you can use the `uninstall` script.

Method 1: Run straight from GitHub by using this command on your Pi

`bash <(curl -s https://raw.githubusercontent.com/jameslawler/pivsmp/main/uninstall.sh)`

Method 2: Clone `https://github.com/jameslawler/pivsmp.git` and run `./uninstall.sh`
