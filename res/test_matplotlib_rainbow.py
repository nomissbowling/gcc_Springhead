#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''test_matplotlib_rainbow
'''

import sys, os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from PIL import Image

def getHSV2RGB(a):
  return (np.array(cm.hsv(a))*255).astype(np.uint8)[:3]

def getColStr(r, g, b):
  '''matplotlib.colors.rgb2hex(rgb)'''
  return '#%02x%02x%02x' % (r, g, b)

def test_matplotlib_rainbow():
  fig = plt.figure(figsize=(6, 4), dpi=96)
  ax = fig.add_subplot(111)

  #im = np.array(list(list([0,0,0,0.8] for _ in range(64)) for _ in range(64)))
  im = np.random.random((64, 64, 4))
  ax.imshow(im, aspect='auto', cmap=cm) # cmap=cm cmap=cm.hsv
  ax.imshow(im, aspect='auto', extent=[100, 228, 100, 228], origin='lower')

  for i in range(0, 360, 4):
    ax.plot(i, i, 'o', color=getColStr(*getHSV2RGB(i / 360.0)))

  ax.plot(np.arange(360) - 30, np.arange(360) - 10, 'm')

  ax.plot(np.arange(360) - 30, np.arange(360), getColStr(*getHSV2RGB(0.5)))

  # ax.plot(np.arange(360) + 10, np.arange(360) - 30, cmap=cm.hsv) # BAD
  ax.set_color_cycle([cm.hsv(_ / 360.0) for _ in range(360)])
  for i in range(360):
    ax.plot(np.arange(i, i + 2) + 10, np.arange(i, i + 2) - 30, linewidth=3)

  # print ax._get_lines.get_next_color() # matplotlib >= 3 ?
  # print ax._get_lines.color_cycle # matplotlib >= 3 ?
  print ax.get_lines()[-1].get_color()
  print ax.get_lines()[-360].get_color()

  ax.set_color_cycle([cm.hsv(_ / 8.0) for _ in range(8)])
  for i in range(8):
    ax.plot(np.arange(360) - 5 - i * 2, np.arange(360) - 30)

  ax.set_xlim([-50, 400])
  ax.set_ylim([-50, 400])
  plt.show()

if __name__ == '__main__':
  test_matplotlib_rainbow()
