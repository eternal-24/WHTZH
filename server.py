import serial
import RPi.GPIO as GPIO

ser = serial.Serial("/dev/serial0", 9600, timeout=1)

GPIO.setmode(GPIO.BOARD)

led_ctrl_channels = [29,31]
led_fb_channels = [33,35]
led_fb1 = led_fb_channels[0]
led_fb2 = led_fb_channels[1]
GPIO.setup(led_ctrl_channels,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(led_fb_channels,GPIO.IN)

ser.write("等待PC发出指令\n")
while True:
    line = ser.readline().decode().strip()
    if not line:
        continue
    if line == "LED_on":
        GPIO.output(led_ctrl_channels,GPIO.HIGH)
        fb1 = GPIO.input(led_fb1)
        print(fb1)
        fb2 = GPIO.input(led_fb2)
        print(fb2)
        ser.write("LED已开启\n")
    elif line == "LED_off":
        GPIO.output(led_ctrl_channels,GPIO.LOW)
        fb1 = GPIO.input(led_fb1)
        print(fb1)
        fb2 = GPIO.input(led_fb2)
        print(fb2)
        ser.write("LED已关闭\n")