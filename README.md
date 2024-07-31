# Thermofisher RadEye Radiation Sensor Logger

This work enables serial communication and logging of data from the G and GN family of RadEye sensors from Thermofisher.  This has been designed for use with Linux machines (primarily Ubuntu), however, the code does not require the Robot Operating System (ROS).

## Installation
### As ZIP File
- Go to the top right under "<> Code" and select the "Download ZIP" option
- Extract the contents to your chosen directory

The code is now ready to use

### Using Git
- Open a terminal and navigate to your desired directory, e.g. /Documents/ would be ```cd ~/Documents/```
- Clone the repository using the command ```git clone https://github.com/DrAndyWest/thermofisher_logger.git```

The code is now ready to use

## How to Use (Linux)

![Using the G10 gamma probe with a simulated source](docs/figures/G10.jpg)

1. Open a terminal and use the command ```ls /dev/ | grep ttyUSB```, this should list any usb devices and the port they are connected to (e.g. /dev/ttyUSB0)
2. Plug the usb cable into your machine (you do not need the sensor at this point)
3. Repeat the command ```ls /dev/ | grep ttyUSB```, you should notice a new listing (e.g. /dev/ttyUSB1), this represents the port to communicate with
4. Set up your experiment with the necessary simulated or real radiation sources
5. Ensure the sensor is switched on and placed in the dock (with the usb cable attached to the dock)
6. In the terminal, navigate to the location of the python script, e.g. ```cd ~/Documents/thermofisher_logger/```
7. Run the script with ```python radeye_logger.py```, if you need to specify the port use ```--port``` as an argument, e.g. ```python radeye_logger.py --port /dev/ttyUSB1```
8. The script will generate a comma separated .log file (plain text), with each row having the format {time since start, value}

You can open the .log files in a text editor, import them into Excel, or write code to read and analyse the data.
Please note, you may wish to use so-called [udev rules](https://opensource.com/article/18/11/udev) and the ```SYMLINK``` option to ensure the port name is always the same.

# Other Information
## Todo List
- [ ] ensure support for SX family of sensors

# Bugs & Feature Requests
Please report bugs and request features using the [Issue Tracker](https://github.com/DrAndyWest/thermofisher_logger/issues).

