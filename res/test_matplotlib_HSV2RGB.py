#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''test_matplotlib_HSV2RGB
https://stackoverflow.com/questions/10787103/2d-hsv-color-space-in-matplotlib
'''

import sys, os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import hsv_to_rgb

def test_HSV2RGB():
  fig = plt.figure(figsize=(6, 4), dpi=96)
  S, H = np.mgrid[0:1:100j, 0:1:300j]
  V = np.ones_like(S)
  HSV = np.dstack((H, S, V))
  RGB = hsv_to_rgb(HSV)
  plt.imshow(RGB, origin='lower', extent=[0, 360, 0, 1], aspect=120)
  plt.xlabel('H')
  plt.ylabel('S')
  plt.title('$V_{HSV}=1$')
  plt.show()

if __name__ == '__main__':
  test_HSV2RGB()
