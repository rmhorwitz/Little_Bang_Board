"""code.py"""
"""Created by Rickey M Horwitz, Intense Arcade"""
import time
import board
import busio
import digitalio
import adafruit_lis3dh
import adafruit_tlc5947
import analogio
import usb_hid
from joystick_xl.inputs import Axis
from joystick_xl.joystick import Joystick
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

configdata = open("config.txt", "r")

row = configdata.readlines()
for line in row:
    if line.find("acc_deadband") > -1:
        info = line.split()
        acd = int(info[2])
    if line.find("x_acc_gain") > -1:
        info = line.split()
        xag = int(info[2])
    if line.find("y_acc_gain") > -1:
        info = line.split()
        yag = int(info[2])
    if line.find("acc_orientation") > -1:
        info = line.split()
        ao = int(info[2])
    if line.find("plunger_offset") > -1:
        info = line.split()
        po = int(info[2])
    if line.find("plunger_gain") > -1:
        info = line.split()
        pg = int(info[2])
    if line.find("button_01") > -1:
        info = line.split()
        btn_1 = info[2]
    if line.find("button_02") > -1:
        info = line.split()
        btn_2 = info[2]
    if line.find("button_03") > -1:
        info = line.split()
        btn_3 = info[2]
    if line.find("button_04") > -1:
        info = line.split()
        btn_4 = info[2]
    if line.find("button_05") > -1:
        info = line.split()
        btn_5 = info[2]
    if line.find("button_06") > -1:
        info = line.split()
        btn_6 = info[2]
    if line.find("button_07") > -1:
        info = line.split()
        btn_7 = info[2]
    if line.find("button_08") > -1:
        info = line.split()
        btn_8 = info[2]
    if line.find("button_09") > -1:
        info = line.split()
        btn_9 = info[2]
    if line.find("button_10") > -1:
        info = line.split()
        btn_10 = info[2]
    if line.find("button_11") > -1:
        info = line.split()
        btn_11 = info[2]
    if line.find("button_12") > -1:
        info = line.split()
        btn_12 = info[2]
    if line.find("button_13") > -1:
        info = line.split()
        btn_13 = info[2]
    if line.find("button_14") > -1:
        info = line.split()
        btn_14 = info[2]
    if line.find("button_15") > -1:
        info = line.split()
        btn_15 = info[2]
    if line.find("button_16") > -1:
        info = line.split()
        btn_16 = info[2]
    if line.find("outp_01") > -1:
        info = line.split()
        outp_1 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_02") > -1:
        info = line.split()
        outp_2 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_03") > -1:
        info = line.split()
        outp_3 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_04") > -1:
        info = line.split()
        outp_4 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_05") > -1:
        info = line.split()
        outp_5 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_06") > -1:
        info = line.split()
        outp_6 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_07") > -1:
        info = line.split()
        outp_7 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_08") > -1:
        info = line.split()
        outp_8 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_09") > -1:
        info = line.split()
        outp_9 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_10") > -1:
        info = line.split()
        outp_10 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_11") > -1:
        info = line.split()
        outp_11 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_12") > -1:
        info = line.split()
        outp_12 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_13") > -1:
        info = line.split()
        outp_13 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_14") > -1:
        info = line.split()
        outp_14 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_15") > -1:
        info = line.split()
        outp_15 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_16") > -1:
        info = line.split()
        outp_16 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_17") > -1:
        info = line.split()
        outp_17 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_18") > -1:
        info = line.split()
        outp_18 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_19") > -1:
        info = line.split()
        outp_19 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_20") > -1:
        info = line.split()
        outp_20 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_21") > -1:
        info = line.split()
        outp_21 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_22") > -1:
        info = line.split()
        outp_22 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_23") > -1:
        info = line.split()
        outp_23 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_24") > -1:
        info = line.split()
        outp_24 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_25") > -1:
        info = line.split()
        outp_25 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_26") > -1:
        info = line.split()
        outp_26 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_27") > -1:
        info = line.split()
        outp_27 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_28") > -1:
        info = line.split()
        outp_28 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_29") > -1:
        info = line.split()
        outp_29 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_30") > -1:
        info = line.split()
        outp_30 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_31") > -1:
        info = line.split()
        outp_31 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_32") > -1:
        info = line.split()
        outp_32 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_33") > -1:
        info = line.split()
        outp_33 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_34") > -1:
        info = line.split()
        outp_34 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_35") > -1:
        info = line.split()
        outp_35 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_36") > -1:
        info = line.split()
        outp_36 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_37") > -1:
        info = line.split()
        outp_37 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_38") > -1:
        info = line.split()
        outp_38 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_39") > -1:
        info = line.split()
        outp_39 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_40") > -1:
        info = line.split()
        outp_40 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_41") > -1:
        info = line.split()
        outp_41 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_42") > -1:
        info = line.split()
        outp_42 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_43") > -1:
        info = line.split()
        outp_43 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_44") > -1:
        info = line.split()
        outp_44 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_45") > -1:
        info = line.split()
        outp_45 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_46") > -1:
        info = line.split()
        outp_46 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_47") > -1:
        info = line.split()
        outp_47 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
    if line.find("outp_48") > -1:
        info = line.split()
        outp_48 = tuple(
            (int(info[2]), int(info[4]), int(info[6]), int(info[8]), int(info[10]))
        )
output_dat = tuple(
    (
        outp_1,
        outp_2,
        outp_3,
        outp_4,
        outp_5,
        outp_6,
        outp_7,
        outp_8,
        outp_9,
        outp_10,
        outp_11,
        outp_12,
        outp_13,
        outp_14,
        outp_15,
        outp_16,
        outp_17,
        outp_18,
        outp_19,
        outp_20,
        outp_21,
        outp_22,
        outp_23,
        outp_24,
        outp_25,
        outp_26,
        outp_27,
        outp_28,
        outp_29,
        outp_30,
        outp_31,
        outp_22,
        outp_33,
        outp_34,
        outp_35,
        outp_36,
        outp_37,
        outp_38,
        outp_39,
        outp_40,
        outp_41,
        outp_42,
        outp_43,
        outp_44,
        outp_45,
        outp_46,
        outp_47,
        outp_48,
    )
)
button_dat = tuple(
    (
        btn_1,
        btn_2,
        btn_3,
        btn_4,
        btn_5,
        btn_6,
        btn_7,
        btn_8,
        btn_9,
        btn_10,
        btn_11,
        btn_12,
        btn_13,
        btn_14,
        btn_15,
        btn_16,
    )
)
parameter_dat = tuple((acd, xag, yag, po, pg))

# time.sleep(1.0)
i2c = busio.I2C(board.GP5, board.GP4)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
lis3dh.range = adafruit_lis3dh.RANGE_2_G
lis3dh.range = adafruit_lis3dh.RANGE_2_G
lis3dh.data_rate = adafruit_lis3dh.DATARATE_100_HZ
error_lis3dh = 0
error_flag = 0

# Define pins connected to the TLC5947
SCK = board.GP18  # SCK
MOSI = board.GP19  # MOSI
LATCH = digitalio.DigitalInOut(board.GP17)

# Initialize SPI bus.
spi = busio.SPI(clock=SCK, MOSI=MOSI)

# Initialize TLC5947
tlc5947 = adafruit_tlc5947.TLC5947(spi, LATCH)

# intialize all button status flags to 0
btp_1 = 0
btp_2 = 0
btp_3 = 0
btp_4 = 0
btp_5 = 0
btp_6 = 0
btp_7 = 0
btp_8 = 0
btp_9 = 0
btp_10 = 0
btp_11 = 0
btp_12 = 0
btp_13 = 0
btp_14 = 0
btp_15 = 0
btp_16 = 0
time_a = 0


class x_acc0:
    value = int(lis3dh.acceleration.x * parameter_dat[1])


class y_acc0:
    value = int(lis3dh.acceleration.y * parameter_dat[2])


class x_acc1:
    value = int(lis3dh.acceleration.y * parameter_dat[2])


class y_acc1:
    value = int(lis3dh.acceleration.x * parameter_dat[1])


Plunger = analogio.AnalogIn(board.A2)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
error_count = int(0)
button_1 = digitalio.DigitalInOut(board.GP0)
button_1.direction = digitalio.Direction.INPUT
button_1.pull = digitalio.Pull.DOWN

button_2 = digitalio.DigitalInOut(board.GP1)
button_2.direction = digitalio.Direction.INPUT
button_2.pull = digitalio.Pull.DOWN

button_3 = digitalio.DigitalInOut(board.GP2)
button_3.direction = digitalio.Direction.INPUT
button_3.pull = digitalio.Pull.DOWN

button_4 = digitalio.DigitalInOut(board.GP3)
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

button_15 = digitalio.DigitalInOut(board.GP20)
button_15.direction = digitalio.Direction.INPUT
button_15.pull = digitalio.Pull.DOWN

button_16 = digitalio.DigitalInOut(board.GP21)
button_16.direction = digitalio.Direction.INPUT
button_16.pull = digitalio.Pull.DOWN

js = Joystick()
if ao == 0 or ao == 2:
    js.add_input(
        Axis(x_acc0, int(parameter_dat[0]), -32000, 32000),
        # the first arg is the dead band, this keeps the table from shaking.
        Axis(y_acc0, int(parameter_dat[0]), -32000, 32000),
        # 2nd is the lowest int, and the 3rd is the highest int
        Axis(Plunger),
    )
if ao == 1 or ao == 3:
    js.add_input(
        Axis(x_acc1, int(parameter_dat[0]), -32000, 32000),
        # the first arg is the dead band, this keeps the table from shaking.
        Axis(y_acc1, int(parameter_dat[0]), -32000, 32000),
        # 2nd is the lowest int, and the 3rd is the highest int
        Axis(Plunger),
    )
print(ao)
while True:
    if error_flag == 0:
        try:
            if ao == 0:
                x_acc0.value = int((lis3dh.acceleration.x) * int(parameter_dat[1]))
                y_acc0.value = int((lis3dh.acceleration.y) * int(parameter_dat[2]))
            if ao == 1:
                x_acc1.value = int((lis3dh.acceleration.y) * int(parameter_dat[2]))
                y_acc1.value = int((lis3dh.acceleration.x) * int(parameter_dat[1]))
            if ao == 2:
                x_acc0.value = int((lis3dh.acceleration.x) * int(parameter_dat[1]))
                y_acc0.value = -1 * (
                    int((lis3dh.acceleration.y) * int(parameter_dat[2]))
                )
            if ao == 3:
                x_acc1.value = -1 * (
                    int((lis3dh.acceleration.y) * int(parameter_dat[2]))
                )
                y_acc1.value = int((lis3dh.acceleration.x) * int(parameter_dat[1]))

        except OSError:
            error_flag = 1
            error_count = error_count + 1
            print("OSError counted", error_count, " time_a= ", time_a)
        except ValueError:
            error_flag = 1
            error_count = error_count + 1
            print("ValueError Reset!")

    if x_acc0 == 0 and y_acc0 == 0 and x_acc1 == 0 and y_acc1 == 0:
        time.sleep(0.1)
        print("lis3dh is dead, re-initializing")
        try:
            lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
            lis3dh.range = adafruit_lis3dh.RANGE_2_G
            lis3dh.data_rate = adafruit_lis3dh.DATARATE_100_HZ
            if ao == 0:
                x_acc0.value = int((lis3dh.acceleration.x) * int(parameter_dat[1]))
                y_acc0.value = int((lis3dh.acceleration.y) * int(parameter_dat[2]))
            if ao == 1:
                x_acc1.value = int((lis3dh.acceleration.y) * int(parameter_dat[2]))
                y_acc1.value = int((lis3dh.acceleration.x) * int(parameter_dat[1]))
            if ao == 2:
                x_acc0.value = int((lis3dh.acceleration.x) * int(parameter_dat[1]))
                y_acc0.value = -1 * (
                    int((lis3dh.acceleration.y) * int(parameter_dat[2]))
                )
            if ao == 3:
                x_acc1.value = -1 * (
                    int((lis3dh.acceleration.y) * int(parameter_dat[2]))
                )
                y_acc1.value = int((lis3dh.acceleration.x) * int(parameter_dat[1]))
        except ValueError:
            error_flag = 1
    try:
        js.update()
    except OSError:
        print("HID Error"), error_count
        time.sleep(0.1)

    if button_1.value:
        btp_1 = 1
        print(button_dat[0])
        keyboard.press(getattr(Keycode, button_dat[0]))
        time.sleep(0.025)
    if not (button_1.value):
        if btp_1 == 1:
            keyboard.release(getattr(Keycode, button_dat[0]))
            btp_1 = 0
    if button_2.value:
        btp_2 = 1
        print(button_dat[1])
        keyboard.press(getattr(Keycode, button_dat[1]))
        time.sleep(0.025)
    if not (button_2.value):
        if btp_2 == 1:
            keyboard.release(getattr(Keycode, button_dat[1]))
            btp_2 = 0
    if button_3.value:
        btp_3 = 1
        keyboard.press(getattr(Keycode, button_dat[2]))
        time.sleep(0.025)
    if not (button_3.value):
        if btp_3 == 1:
            keyboard.release(getattr(Keycode, button_dat[2]))
            lc = 0
    if button_4.value:
        btp_4 = 1
        keyboard.press(getattr(Keycode, button_dat[3]))
        time.sleep(0.025)
    if not button_4.value:
        if btp_4 == 1:
            keyboard.release(getattr(Keycode, button_dat[3]))
            btp_4 == 0
    if button_5.value:
        btp_5 = 1
        keyboard.press(getattr(Keycode, button_dat[4]))
        time.sleep(0.025)
    if not button_5.value:
        if btp_5 == 1:
            keyboard.release(getattr(Keycode, button_dat[4]))
            btp_5 = 0

    if button_6.value:
        btp_6 = 1
        keyboard.press(getattr(Keycode, button_dat[5]))
        time.sleep(0.025)
    if not button_6.value:
        if btp_6 == 1:
            keyboard.release(getattr(Keycode, button_dat[5]))
            btp_6 = 0

    if button_7.value:
        btp_7 = 1
        keyboard.press(getattr(Keycode, button_dat[6]))
        time.sleep(0.025)
    if not button_7.value:
        if btp_7 == 1:
            keyboard.release(getattr(Keycode, button_dat[6]))
            btp_7 = 0

    if button_8.value:
        btp_8 = 1
        keyboard.press(getattr(Keycode, button_dat[7]))
        time.sleep(0.025)
    if not button_8.value:
        if btp_8 == 1:
            keyboard.release(getattr(Keycode, button_dat[7]))
            btp_8 = 0

    if button_9.value:
        btp_9 = 1
        keyboard.press(getattr(Keycode, button_dat[8]))
        time.sleep(0.025)
    if not button_9.value:
        if btp_9 == 1:
            keyboard.release(getattr(Keycode, button_dat[8]))
            btp_9 = 0

    if button_10.value:
        btp_10 = 1
        keyboard.press(getattr(Keycode, button_dat[9]))
        time.sleep(0.025)
    if not button_10.value:
        if btp_10 == 1:
            keyboard.release(getattr(Keycode, button_dat[9]))
            btp_10 = 0

    if button_11.value:
        btp_11 = 1
        keyboard.press(getattr(Keycode, button_dat[10]))
        time.sleep(0.025)
    if not button_11.value:
        if btp_11 == 1:
            keyboard.release(getattr(Keycode, button_dat[10]))
            btp_11 = 0

    if button_12.value:
        btp_12 = 1
        keyboard.press(getattr(Keycode, button_dat[11]))
        time.sleep(0.025)
    if not button_12.value:
        if btp_12 == 1:
            keyboard.release(getattr(Keycode, button_dat[11]))
            btp_12 = 0

    if button_13.value:
        btp_13 = 1
        keyboard.send(getattr(Keycode, button_dat[12]))
        time.sleep(0.025)
    if not button_13.value:
        if btp_13 == 1:
            keyboard.release(getattr(Keycode, button_dat[12]))
            btp_13 = 0

    if button_14.value:
        btp_14 = 1
        keyboard.send(getattr(Keycode, button_dat[13]))
        time.sleep(0.025)
    if not button_14.value:
        if btp_14 == 1:
            keyboard.release(getattr(Keycode, button_dat[13]))
            btp_14 = 0

    if button_15.value:
        btp_15 = 1
        keyboard.send(getattr(Keycode, button_dat[14]))
        time.sleep(0.025)
    if not button_15.value:
        if btp_15 == 1:
            keyboard.release(getattr(Keycode, button_dat[14]))
            btp_15 = 0

    if button_16.value:
        btp_16 = 1
        keyboard.send(getattr(Keycode, button_dat[15]))
        time.sleep(0.025)
    if not button_16.value:
        if btp_16 == 1:
            keyboard.release(getattr(Keycode, button_dat[15]))
            btp_16 = 0
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

    # time.sleep(0.005)
