"""code.py"""
"""Created by Rickey M Horwitz, Intense Arcade"""
import time
import supervisor
import board
import busio
import digitalio
import adafruit_lis3dh
import analogio
import usb_hid
from joystick_xl.inputs import Axis
from joystick_xl.joystick import Joystick
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
time.sleep(1.0)
i2c = busio.I2C(board.GP1, board.GP0)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
lis3dh.range = adafruit_lis3dh.RANGE_2_G
lis3dh.data_rate = adafruit_lis3dh.DATARATE_100_HZ
error_lis3dh = 0
error_flag = 0
btn_1 = 0
btn_2 = 0
btn_3 = 0
btn_4 = 0
btn_5 = 0
btn_6 = 0
btn_7 = 0
btn_8 = 0
btn_9 = 0
btn_10 = 0
btn_11 = 0
btn_12 = 0
btn_13 = 0
btn_14 = 0
btn_15 = 0
btn_16 = 0
time_a = 0

class x_acc:
    value = int(lis3dh.acceleration.x * -3500)

class y_acc:
    value = int(lis3dh.acceleration.y * 3500)

Plunger = analogio.AnalogIn(board.A2)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
error_count = int(0)
button_1 = digitalio.DigitalInOut(board.GP2)
button_1.direction = digitalio.Direction.INPUT
button_1.pull = digitalio.Pull.DOWN

button_2 = digitalio.DigitalInOut(board.GP3)
button_2.direction = digitalio.Direction.INPUT
button_2.pull = digitalio.Pull.DOWN

button_3 = digitalio.DigitalInOut(board.GP4)
button_3.direction = digitalio.Direction.INPUT
button_3.pull = digitalio.Pull.DOWN

button_4 = digitalio.DigitalInOut(board.GP5)
button_4.direction = digitalio.Direction.INPUT
button_4.pull = digitalio.Pull.DOWN

button_5 = digitalio.DigitalInOut(board.GP6)
button_5.direction = digitalio.Direction.INPUT
button_5.pull = digitalio.Pull.DOWN

button_6 = digitalio.DigitalInOut(board.GP7)
button_6.direction = digitalio.Direction.INPUT
button_6.pull = digitalio.Pull.DOWN

button_7 = digitalio.DigitalInOut(board.GP8)
button_7.direction = digitalio.Direction.INPUT
button_7.pull = digitalio.Pull.DOWN

button_8 = digitalio.DigitalInOut(board.GP9)
button_8.direction = digitalio.Direction.INPUT
button_8.pull = digitalio.Pull.DOWN

button_9 = digitalio.DigitalInOut(board.GP10)
button_9.direction = digitalio.Direction.INPUT
button_9.pull = digitalio.Pull.DOWN

button_10 = digitalio.DigitalInOut(board.GP11)
button_10.direction = digitalio.Direction.INPUT
button_10.pull = digitalio.Pull.DOWN

button_11 = digitalio.DigitalInOut(board.GP12)
button_11.direction = digitalio.Direction.INPUT
button_11.pull = digitalio.Pull.DOWN

button_12 = digitalio.DigitalInOut(board.GP13)
button_12.direction = digitalio.Direction.INPUT
button_12.pull = digitalio.Pull.DOWN

button_13 = digitalio.DigitalInOut(board.GP14)
button_13.direction = digitalio.Direction.INPUT
button_13.pull = digitalio.Pull.DOWN

button_14 = digitalio.DigitalInOut(board.GP15)
button_14.direction = digitalio.Direction.INPUT
button_14.pull = digitalio.Pull.DOWN

button_15 = digitalio.DigitalInOut(board.GP16)
button_15.direction = digitalio.Direction.INPUT
button_15.pull = digitalio.Pull.DOWN

button_16 = digitalio.DigitalInOut(board.GP17)
button_16.direction = digitalio.Direction.INPUT
button_16.pull = digitalio.Pull.DOWN

js = Joystick()
js.add_input(
    Axis(x_acc, 1000, -32000, 32000), # the first arg is the dead band, this keeps the table from shaking.
    Axis(y_acc, 1000, -32000, 32000), #2nd is the lowest int, and the 3rd is the highest int
    Axis(Plunger),
)
while True:

            # I set up a clock for 10ms sampling of the X/Y acceleration.  The clock rolls over every
            # couple hours, so check to see if my time stamp (time_a) is larger than the clock ticks, that means it rolled over.
    if supervisor.ticks_ms() - 10 > time_a or time_a - 1000 > supervisor.ticks_ms():
        if error_flag == 0:
            try:
                x_acc.value = int((lis3dh.acceleration.x) * -3500)
                y_acc.value = int((lis3dh.acceleration.y) * 3500)
                time_a = supervisor.ticks_ms()
            except OSError:
                error_flag = 1
                error_count = error_count + 1
                print("OSError counted", error_count, " time_a= ", time_a)
            except ValueError:
                error_flag = 1
                error_count = error_count + 1
                print("ValueError Reset!")

    if x_acc == 0 and y_acc == 0:
        time.sleep(0.1)
        print("lis3dh is dead, re-initializing")
        try:
            lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
            lis3dh.range = adafruit_lis3dh.RANGE_2_G
            lis3dh.data_rate = adafruit_lis3dh.DATARATE_100_HZ
            x_acc.value = int((lis3dh.acceleration.x) * -3500)
            y_acc.value = int((lis3dh.acceleration.y) * 3500)
        except ValueError:
            error_flag = 1
    try:
        js.update()
    except OSError:
        print("HID Error"), error_count
        time.sleep(0.1)

    if button_1.value:
        btn_1 = 1
        keyboard.press(Keycode.LEFT_SHIFT)
        time.sleep(0.025)
    if not (button_1.value):
        if btn_1 == 1:
            keyboard.release(Keycode.LEFT_SHIFT)
            btn_1 = 0
    if button_2.value:
        btn_2 = 1
        keyboard.press(Keycode.RIGHT_SHIFT)
        time.sleep(0.025)
    if not (button_2.value):
        if btn_2 == 1:
            keyboard.release(Keycode.RIGHT_SHIFT)
            btn_2 = 0
    if button_3.value:
        btn_3 = 1
        keyboard.press(Keycode.LEFT_CONTROL)
        time.sleep(0.025)
    if not (button_3.value):
        if btn_3 == 1:
            keyboard.release(Keycode.LEFT_CONTROL)
            lc = 0
    if button_4.value:
        btn_4 = 1
        keyboard.press(Keycode.RIGHT_CONTROL)
        time.sleep(0.025)
    if not button_4.value:
        if btn_4 == 1:
            keyboard.release(Keycode.RIGHT_CONTROL)
            btn_4 == 0
    if button_5.value:
        btn_5 = 1
        keyboard.press(Keycode.ONE)
        time.sleep(0.025)
    if not button_5.value:
        if btn_5 == 1:
            keyboard.release(Keycode.ONE)
            btn_5 = 0

    if button_6.value:
        btn_6 = 1
        keyboard.press(Keycode.FIVE)
        time.sleep(0.025)
    if not button_6.value:
        if btn_6 == 1:
            keyboard.release(Keycode.FIVE)
            btn_6 = 0

    if button_7.value:
        btn_7 = 1
        keyboard.press(Keycode.FOUR)
        time.sleep(0.025)
    if not button_7.value:
        if btn_7 == 1:
            keyboard.release(Keycode.FOUR)
            btn_7 = 0

    if button_8.value:
        btn_8 = 1
        keyboard.press(Keycode.ENTER)
        time.sleep(0.025)
    if not button_8.value:
        if btn_8 == 1:
            keyboard.release(Keycode.ENTER)
            btn_8 = 0

    if button_9.value:
        btn_9 = 1
        keyboard.press(Keycode.Q)
        time.sleep(0.025)
    if not button_9.value:
        if btn_9 == 1:
            keyboard.release(Keycode.Q)
            btn_9 = 0

    if button_10.value:
        btn_10 = 1
        keyboard.press(Keycode.EQUALS)
        time.sleep(0.025)
    if not button_10.value:
        if btn_10 == 1:
            keyboard.release(Keycode.EQUALS)
            btn_10 = 0

    if button_11.value:
        btn_11 = 1
        keyboard.press(Keycode.MINUS)
        time.sleep(0.025)
    if not button_11.value:
        if btn_11 == 1:
            keyboard.release(Keycode.MINUS)
            btn_11 = 0

    if button_12.value:
        btn_12 = 1
        keyboard.press(Keycode.F11)
        time.sleep(0.025)
    if not button_12.value:
        if btn_12 == 1:
            keyboard.release(Keycode.F11)
            btn_12 = 0

    if button_13.value:
        btn_13 = 1
        keyboard.send(Keycode.T)
        time.sleep(0.025)
    if not button_13.value:
        if btn_13 == 1:
            keyboard.release(Keycode.T)
            btn_13 = 0

    if button_14.value:
        btn_14 = 1
        keyboard.send(Keycode.FIVE)
        time.sleep(0.025)
    if not button_14.value:
        if btn_14 == 1:
            keyboard.release(Keycode.FIVE)
            btn_14 = 0

    if button_15.value:
        btn_15 = 1
        keyboard.send(Keycode.FOUR)
        time.sleep(0.025)
    if not button_15.value:
        if btn_15 == 1:
            keyboard.release(Keycode.FOUR)
            btn_15 = 0

    if button_16.value:
        btn_16 = 1
        keyboard.send(Keycode.ENTER)
        time.sleep(0.025)
    if not button_16.value:
        if btn_16 == 1:
            keyboard.release(Keycode.ENTER)
            btn_16 = 0
    if error_flag == 1:
        error_lis3dh = error_lis3dh + 1

    if error_lis3dh == 250:  # this is equivent to 1.25 seconds
        print("error_flag:", error_flag, "Error_lis3dh", error_lis3dh)
        error_lis3dh = 0
        error_flag = 0
        try:
            lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
            lis3dh.range = adafruit_lis3dh.RANGE_2_G
            lis3dh.data_rate = adafruit_lis3dh.DATARATE_100_HZ
            error_lis3dh = 0
            error_flag = 0
        except ValueError:
            error_flag = 1

    time.sleep(0.005)
