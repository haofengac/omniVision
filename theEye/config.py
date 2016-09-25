import cv, cv2
import time

#
# BBoxes must be in the format:
# ( (topleft_x), (topleft_y) ), ( (bottomright_x), (bottomright_y) ) )

import thread, time
import hashlib
import numpy as np

TOP = 0
BOTTOM = 1
LEFT = 0
RIGHT = 1

CAPTURE_WIDTH = 320
CAPTURE_HEIGHT = 240
display_ratio = 2.5

RECOGNIZE_THRESHOLD = 50