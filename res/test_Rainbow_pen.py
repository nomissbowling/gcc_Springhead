#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''test_Rainbow_pen
'''

import sys, os
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

FN_OUT = 'rainbow_pen_320x240.png'

def mk_col(w, h, x, y):
  a = 255
  i = int(7 * y / h)
  if i == 0: c, u, v = (192, 0, 0), (32, 0, 0), (0, 32, 0) # R
  elif i == 1: c, u, v = (192, 96, 0), (0, -32, 0), (0, 32, 0) # O-
  elif i == 2: c, u, v = (192, 192, 0), (0, -32, 0), (-32, 0, 0) # Y
  elif i == 3: c, u, v = (0, 192, 0), (64, 0, 0), (0, 0, 64) # G
  elif i == 4: c, u, v = (0, 192, 192), (0, 0, -64), (0, -64, 0) # C
  elif i == 5: c, u, v = (0, 0, 192), (0, 64, 0), (32, 0, 0) # B
  elif i == 6: c, u, v = (96, 0, 192), (-32, 0, 0), (32, 0, 0) # M-
  return (i, a, c, u, v)

def mk_dum(w, h, x, y):
  # return (64, 64, 64, 192)
  i, a, (r, g, b), u, v = mk_col(w, h, x, y)
  return (r, g, b, a)

def mk_rainbow(w, h, x, y):
  # return (x % 256, y % 256, 128, 255)
  i, a, (r, g, b), u, v = mk_col(w, h, x, y)
  d = h / 7.0
  z = int(y - i * d)
  e = d / 3.0
  f = 1 if z < e else (-1 if z > 2*e else 0)
  rgb = np.array((r, g, b))
  if f > 0: rgb += np.array(u)
  if f < 0: rgb += np.array(v)
  r, g, b = rgb
  if x < w / 4:
    j, k = 2.0 * d * x / w, d / 2.0
    t = z + j < k or z - j > k
    if x < w / 36 or t: return (255, 255, 255, 0) # transparent
    if x < w / 12: return (r, g, b, a)
    else: return (224, 128, 0, 255) # light brown
  return (r, g, b, a)

def rainbow_pen(w, h):
  fig = plt.figure(figsize=(6, 4), dpi=96)

  dm = np.ndarray((h, w, 4), dtype=np.uint8)
  for y in range(h):
    for x in range(w):
      dm[y][x] = mk_dum(w, h, x, y)
  dum = Image.fromarray(dm[::-1,:,:], 'RGBA')

  im = np.ndarray((h, w, 4), dtype=np.uint8)
  for y in range(h):
    for x in range(w):
      im[y][x] = mk_rainbow(w, h, x, y)
  img = Image.fromarray(im[::-1,:,:], 'RGBA')
  Image.fromarray(im, 'RGBA').save(FN_OUT, 'PNG')

  ax = fig.add_subplot(231)
  ax.imshow(img)
  ax = fig.add_subplot(232)
  ax.imshow(img.convert('L'), cmap='gray', vmin=0, vmax=255)
  ax = fig.add_subplot(233)
  ax.imshow(img.convert('L')) # auto heatmap

  ax = fig.add_subplot(234)
  ax.imshow(img.convert('YCbCr')) # ok ?
  ax = fig.add_subplot(235)
  ax.imshow(dum) # img.convert('LAB')) # not supported on PIL <= py 2.5 ?
  ax = fig.add_subplot(236)
  ax.imshow(dum) # img.convert('HSV')) # not supported on PIL <= py 2.5 ?

  plt.show()

if __name__ == '__main__':
  rainbow_pen(320, 240)
