from g733 import LogitechG733
import main

class MenuActions:
    def __init__(self):
        self.menu()

    def menu(self):
        menu_elements = {
            '1': self.get_battery_percentage,
            '2': self.set_led_color,
            '3': self.power_off_leds,
        }

        while True:
            print("1. Get battery percentage")
            print("2. Set LED color")
            print("3. Power off LEDs")
            print("q. Exit")
            choice = input("Choose an option: ")

            if choice == 'q':
                break
            else:
                menu_elements[choice]()

    def get_battery_percentage(self):
        g733 = main.g733
        charge_percentage = g733.get_charge_percentage()
        print("Battery percentage: ", charge_percentage, "%")


    def set_led_color(self):
        g733 = main.g733
        print("Set the color of the LED")
        print("RGB values from 0 to 255")
        red = int(input("Red Value:"))
        green = int(input("Green Value: "))
        blue = int(input("Blue Value: "))

        g733.set_led_color(red, green, blue)
        print("LED color set to", red, green, blue)
    
    def power_off_leds(self):
        g733 = main.g733
        g733.set_led_color(0, 0, 0)
        print("LEDs turned off")