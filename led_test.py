import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
led_ctrl_channels = [29,31]
led_fb_channels = [33,35]
GPIO.setup(led_ctrl_channels,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(led_fb_channels,GPIO.IN)
GPIO.output(led_ctrl_channels,GPIO.HIGH)