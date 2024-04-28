"""boot.py"""
import usb_hid
from joystick_xl.hid import create_joystick

# enable default CircuitPython USB HID devices as well as JoystickXL
usb_hid.enable(
  (
    usb_hid.Device.KEYBOARD,
    usb_hid.Device.MOUSE,
    usb_hid.Device.CONSUMER_CONTROL,
    create_joystick(axes=3, buttons=0, hats=0),
  )
)