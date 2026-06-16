# How Raspberry Pi connects to SimpleRTK2B

This file is our notes on how data is recorded from the ardusimple
GPS sensor and sent to the Raspberry Pi. 

## Communication interface

All info is sent through UART. It's a serial connection to the Raspberry Pi
with a baud rate of `115200`.

The tutorial given by ardusimple focuses on the UART connection to the Pi
on pins 14 and 15. They are the Tx and Rx pins for the ZED-F9P chip.
There are other options, like the xBee connection. The connection is used
for different communication methods that are added on later.
The device would have to be reconfigured to use them, which can be done
using U-center with any computer and a usb connection.

## Configuration Intro

The receiver comes pre-configured as a `Rover`. This is an object whose
current location needs to be tracked. This is different from what we want it
to do. We want it to act as a base station to calculated the TEC (Total
Electron Content).

Currently, data sent over UART is given as NMEA messages. We want the raw data
captured by the GPS antenna. We want the UBX protocol sent over instead.
This is done by navigating to u-center and configuring to send
`UBX-RXM-RAWX` and `UBX-RXM-SFRBX` data.

Once configured, then we can collect data to process later.

## References

This information was taken from these articles:

- [How to connect your SimpleRTK2B to your Raspberry Pi](www.ardusimple.com/connect-your-simplertk2b-to-a-raspberry-pi/)

- [User Guide: simpleRTK2B Budget](https://www.ardusimple.com/user-guide-simplertk2b-budget/)

- [How to Configure u-blox ZED-F9P](https://www.ardusimple.com/how-to-configure-ublox-zed-f9p/)

- [Collecting Raw UBlox Data with RTKLIB](https://rtklibexplorer.wordpress.com/2016/02/03/collecting-raw-gps-data-with-rtklib/)
