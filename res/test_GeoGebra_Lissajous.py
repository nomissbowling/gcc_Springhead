#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''test_GeoGebra_Lissajous
'''

import sys, os
import numpy as np
from matplotlib import pyplot as plt

def test_GeoGebra_Lissajous():
  fig = plt.figure(figsize=(6, 4), dpi=96)
  r, c = 1, 2
  ax = [[fig.add_subplot(r, c, y*c+x+1) for x in range(c)] for y in range(r)]
  ax[0][0].plot([1,2,3],[4,5,6])
  T = np.arange(-np.pi, np.pi, 0.005)
  X, Y, O = [], [], []
  fp = open('merry_64.dft', 'rb')
  for l in fp.readlines():
    p = map(float, l.rstrip().lstrip().split())
    O.append(p)
  fp.close()
  X = reduce(lambda a, b:
    a + O[b][0] * np.cos(b * T) + O[b][1] * np.sin(b * T), xrange(len(O)), 0)
  Y = reduce(lambda a, b:
    a + O[b][2] * np.cos(b * T) + O[b][3] * np.sin(b * T), xrange(len(O)), 0)
  ax[0][1].plot(X, Y, 'g') # X(-400<->0), Y(-200<->310)
  plt.show()

if __name__ == '__main__':
  test_GeoGebra_Lissajous()
