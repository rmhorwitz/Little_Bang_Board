# Little_Bang_Board
This project is for a Virtual Pinball game controller based on a Rasberry Pi Pico called thew Little Bang Board.  The Little Bang Board is the Open Source DIY version of the Baby Bang Board which uses SMT and JST connectors, it is intented for commercial use by Intense Arcade.  The Little Bang Board provides a virtual ball plunger using the game controller Z axis of a joystick output.  An accelerometer provides X/Y movement to the applicable game controller X/Y joystick output. A true USB keyboard HID emulation provides 16 buttons that can emulate any key.  Basic pinball game controllers can cost anywhere from $40 to $125. The Little Bang Board will set you back $10 and will be as good if not better than the more expensive competition. This project can also be purchased as a complete kit for under $20.  The project is offered as is, and free to copy and use.  If used for profit, all I ask is that the project name not be changed.  
Items in this project that I am providing include Instructions, BOM, PCB fab files (gerbers and drill files) links to Adafruit CircuitPython for Pico, links to Adafruit CircuitPython libraries, schematics, config.txt, Code.py -Main Code, and Boot.py -boot code.  Alternately, I am including a sample script for using Pinscape Pico which is the preferred software for this project. For information and code download concerning MJR's Pinscape for Pico please follow his GitHub page at https://github.com/mjrgh/PinscapePico.  Please enjoy this project. 
Little Bang Board Version 2 has been released.  This new design has the following changes:
JST input/button connector have been replaced with two, ten pin standard terminal blocks
Two additional Inputs for a total of 18
All inputs are pulled high for use of a common ground
Support for AD1115 ADC Module.  This makes this project in-line with MJR's Pinscape Pico project
Support for either LIS3DH or MMA485X Accelerometers, circuit supports interupts for both modules 
Expansion port was modified to support MJR's Pinscape Pico DIY Power Board

