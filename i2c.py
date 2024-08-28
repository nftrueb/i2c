import RPi.GPIO as GPIO 

class Bus: 

    def __init__(pin): 
        self.pin = pin 
        GPIO.setmode(GPIO.BOARD)

    def send_bytes(self): 
        pass

    def get_ack(self): 
        GPIO.setup(self.pin, GPIO.IN)  
        if GPIO.input(self.pin): 
            print('ERROR: did not get ack after transmission byte')
