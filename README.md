# EduKit3-Bluetooth

Please note: these instructions will only work for 1st edition Wii controllers
i.e. those without Wii motionplus. This is a limitation of the CWiid library.

## Software installation
Run the following command to install the bluetooth service:

`sudo apt-get install --no-install-recommends bluetooth`

Once finished, type:

`sudo service bluetooth status`

You should find that the service is Active

Type the following to scan for bluetooth devices:

`hcitool scan`

Now to find the Wii controller.
Make sure your Wii controller has batteries in it :-)

Type:
`hcitool scan`

and press the 1 and 2 buttons on your Wiimote at the same time.
The blue LEDs on the Wiimote will flash and your controller should be found.
It will have the word "Nintendo" in it if you are using an official controller.


