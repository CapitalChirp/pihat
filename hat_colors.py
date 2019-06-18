#!usr/bin/env python


from sense_hat import SenseHat
sense = SenseHat()

red = (255, 0, 0)
black = (0, 0, 0)

speed = 0.05

message = "This is not a message, this is a call for help please"

sense.show_message(message, speed, text_colour=red, back_colour=black)

sense.clear()
