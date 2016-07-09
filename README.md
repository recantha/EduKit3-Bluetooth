# EduKit3-Bluetooth

## Credits
A big thank you to Matt Hawkins (http://www.raspberrypi-spy.co.uk/) and the Raspberry Pi Foundation for the Bluetooth and CWiid instructions.

## Notes
Please consider these instructions a BETA until they are absorbed and reformatted into the EduKit 3 worksheets.

Please note: these instructions will only work for 1st edition Wii controllers
i.e. those without Wii motionplus. This is a limitation of the CWiid library.

## You will need:
* A Raspberry Pi connected up to the EduKit motor controller board with all the
motors and battery pack connected up. It's assumed that you've worked through
at least as far as worksheet 4.
* A portable power source for the Pi, such as a phone charger battery.
* A USB cable to attach the power source to the Raspberry Pi
* A Wiimote (first edition, without motionplus)
* Bluetooth capability. So, one of:
* * Raspberry Pi 3
* * Raspberry Pi Zero + USB adapter + bluetooth dongle
* * Raspberry Pi (other model) + bluetooth dongle

## Software installation
Run the following command to install the bluetooth service:

`sudo apt-get install --no-install-recommends bluetooth`

Once finished, type:

`sudo service bluetooth status`

You should find that the service is Active

Type the following to scan for bluetooth devices:

`hcitool scan`

## Finding and pairing
Now to find the Wii controller.
Make sure your Wii controller has batteries in it :-)

Type:

`hcitool scan`

and press the 1 and 2 buttons on your Wiimote at the same time.
The blue LEDs on the Wiimote will flash and your controller should be found.
It will have the word "Nintendo" in it if you are using an official controller.

## Python library

The next thing to do is to make sure that Python can connect to the controller.
For this, we use a library called `cwiid`. Install it using the following:

`sudo apt-get install python-cwiid`

Now, get the code from this repository:

`git clone https://github.com/recantha/EduKit3-bluetooth`

Change folder:

`cd EduKit3-bluetooth`

Run the test

`python wii_remote_test.py`

When the script tells you to, press the 1+2 buttons on your Wii remote.
It should connect properly. If it doesn't work, try a bit closer or a bit
further away.

Now for the exciting part. Using the Wii controller to control the robot.
There are two parts to this: With a monitor and headless.

First of all, turn your motor battery pack on!

Now, run the controller script:

`python wii_controller.py`

Follow the instructions to pair the Wii controller again.
Once it has paired, you should find that your robot responds to the arrow
buttons. To quit, press PLUS and MINUS together.

Now, to run headless. For this, you will need an LED. Any one will do.
We're going to do something that's not recommended - using an LED without
a current-resisting resistor. I've tried this myself and it's not caused
any issues. Take an LED and insert the short leg into the driver board's
female header marked GND. Insert the longer, positive, leg into the pin marked
25.

Run the script again:

`python wii_controller.py`

This time, you should notice the LED lighting up when pairing begins
and flashing when the controller is connected. Useful, especially
when you have no idea what's happening 'on screen' - i.e. when you're
running 'headless'.

Now, we need to make the script work on bootup. There are a number of
ways to do this but I've chosen this way because it's slightly easier.

First of all, make sure your Pi boots to desktop:
Go to Menu->Preferences->Raspberry Pi configuration and make sure
that Boot is set to 'To Desktop' and that Auto Login is set to 'Login as user pi'
Click OK to confirm.

Now, open up a terminal and type the following:

`sudo nano ~/.config/lxsession/LXDE-pi/autostart`

At the bottom of the file, add the following:

`@/usr/bin/python /home/pi/EduKit3-bluetooth/wii_controller.py`

Reboot your Pi:
`sudo reboot`

Wait for the Pi to come back up - the LED should light up to tell you to
press 1+2 on the Wii controller. It should flash when it's correctly paired.
If the LED goes off without flashing, you need to reboot the Pi.

## Doing it for real

Now shutdown your Pi by typing:

`sudo halt`

Disconnect your keyboard, mouse, power cable so that your Pi is untethered
and then attach your portable Pi power source.

The Pi should boot up, the LED should light up. As before, press 1+2 on your
Wiimote. The LED should flash to let you know you've done it.

Away you go!

## Contacting me
You can either email me at mike (at) recantha.co.uk or via my blog: http://www.recantha.co.uk/blog/?page_id=610
