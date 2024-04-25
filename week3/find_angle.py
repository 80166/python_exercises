import math
from math import degrees
AB, BC = float(input()), float(input())
mbc = math.atan2(AB, BC)
print(str(round(degrees(mbc))) + "\xb0")