from ssd1306 import OLED 

def main(): 
    print('Hello World') 

    pin = 1 
    address = 0x1E
    oled = OLED(pin, address)

if __name__ == '__main__': 
    main()