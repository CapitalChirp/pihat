#!/usr/bin/env python
# this script will display colors for individual pixles on the Pi HAT
from sense_hat import SenseHat
sense = SenseHat()
import time

sense.set_pixel(0, 0,(255, 0, 0))
sense.set_pixel(1, 0,(255, 0, 0))
sense.set_pixel(2, 0,(255, 0, 0))
sense.set_pixel(3, 0,(255, 0, 0))
sense.set_pixel(4, 0,(255, 0, 0))
sense.set_pixel(5, 0,(255, 0, 0))
sense.set_pixel(6, 0,(255, 0, 0))
sense.set_pixel(7, 0,(255, 0, 0))
sense.set_pixel(0, 1,(247, 119, 18))
sense.set_pixel(1, 1,(247, 119, 18))
sense.set_pixel(2, 1,(247, 119, 18))
sense.set_pixel(3, 1,(247, 119, 18))
sense.set_pixel(4, 1,(247, 119, 18))
sense.set_pixel(5, 1,(247, 119, 18))
sense.set_pixel(6, 1,(247, 119, 18))
sense.set_pixel(7, 1,(247, 119, 18))
sense.set_pixel(0, 2,(255, 237, 0))
sense.set_pixel(1, 2,(255, 237, 0))
sense.set_pixel(2, 2,(255, 237, 0))
sense.set_pixel(3, 2,(255, 237, 0))
sense.set_pixel(4, 2,(255, 237, 0))
sense.set_pixel(5, 2,(255, 237, 0))
sense.set_pixel(6, 2,(255, 237, 0))
sense.set_pixel(7, 2,(255, 237, 0))
sense.set_pixel(0, 3,(0, 255, 0))
sense.set_pixel(1, 3,(0, 255, 0))
sense.set_pixel(2, 3,(0, 255, 0))
sense.set_pixel(3, 3,(0, 255, 0))
sense.set_pixel(4, 3,(0, 255, 0))
sense.set_pixel(5, 3,(0, 255, 0))
sense.set_pixel(6, 3,(0, 255, 0))
sense.set_pixel(7, 3,(0, 255, 0))
sense.set_pixel(0, 4,(0, 255, 255))
sense.set_pixel(1, 4,(0, 255, 255))
sense.set_pixel(2, 4,(0, 255, 255))
sense.set_pixel(3, 4,(0, 255, 255))
sense.set_pixel(4, 4,(0, 255, 255))
sense.set_pixel(5, 4,(0, 255, 255))
sense.set_pixel(6, 4,(0, 255, 255))
sense.set_pixel(7, 4,(0, 255, 255))
sense.set_pixel(0, 5,(0, 0, 255))
sense.set_pixel(1, 5,(0, 0, 255))
sense.set_pixel(2, 5,(0, 0, 255))
sense.set_pixel(3, 5,(0, 0, 255))
sense.set_pixel(4, 5,(0, 0, 255))
sense.set_pixel(5, 5,(0, 0, 255))
sense.set_pixel(6, 5,(0, 0, 255))
sense.set_pixel(7, 5,(0, 0, 255))
sense.set_pixel(0, 6,(182, 18, 191))
sense.set_pixel(1, 6,(182, 18, 191))
sense.set_pixel(2, 6,(182, 18, 191))
sense.set_pixel(3, 6,(182, 18, 191))
sense.set_pixel(4, 6,(182, 18, 191))
sense.set_pixel(5, 6,(182, 18, 191))
sense.set_pixel(6, 6,(182, 18, 191))
sense.set_pixel(7, 6,(182, 18, 191))
sense.set_pixel(0, 7,(255, 0, 255))
sense.set_pixel(1, 7,(255, 0, 255))
sense.set_pixel(2, 7,(255, 0, 255))
sense.set_pixel(3, 7,(255, 0, 255))
sense.set_pixel(4, 7,(255, 0, 255))
sense.set_pixel(5, 7,(255, 0, 255))
sense.set_pixel(6, 7,(255, 0, 255))
sense.set_pixel(7, 7,(255, 0, 255))

time.sleep(1)
sense.clear()
