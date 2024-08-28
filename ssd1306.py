# SSD1306 documentation found at 
# https://github.com/nftrueb/i2c/blob/main/SSD1306.pdf

from i2c import Bus

class OLED: 

    # constants 
    WR_WRITE = 0 
    WR_READ = 1
    DC_COMMAND = 0
    DC_DATA = 1 

    def __init__(pin, address): 
        self.bus = Bus(pin)
        self.address = address 

    def reset(self): 
        pass 

    def write(self, str, x, y): 
        pass 

    def draw(self, img, x, y): 
        pass

        def write_command_bytes(self): 
        pass 

    def write_data_bytes(self): 

        # 1) start condition
        # 2) write initialize byte 
        # 3) receive ack 
        # 4) write control byte 
        # 5) receive ack 
        # 6) write data bytes 
        # 7) receive acks 
        # 8) stop condition

        self.start_cond()

    def get_initialization_byte(self, command=True): 
        b = self.addr << 2
        if command: 
            b |= 0x2
        b |= WR_WRITE
        return b

    def start_cond(self): 
        GPIO.setup(self.pin, GPIO.OUT) 
        GPIO.output(self.pin, GPIO.LOW)


    def stop_cond(self): 
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

