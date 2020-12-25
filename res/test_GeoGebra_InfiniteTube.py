#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''test_GeoGebra_InfiniteTube
https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
https://matplotlib.org/search.html?q=cmap
http://taustation.com/mplot3d-axes3d-overview/
https://qiita.com/kazetof/items/c0204f197d394458022a
https://myscitech.hatenablog.com/entry/2019/12/09/210000
https://sabopy.com/py/matplotlib-3d-50/
https://yolo.love/matplotlib/mplot3d/
------------------------------------------------------------------------
(old) py 2.5
ax = Axes3D(fig) # OK
ax.set_aspect('equal') # OK (must be matplotlib < 3.1.0)
x, y, z = [np.array(_) for _ in ([1,0,3], [4,5,6], [7,8,9])]
ax.plot(x, y, z, 'g') # OK 3d line or curve
ax.scatter(x, y, z - 1, 'rx') # OK 3d scatter
ax.scatter3D(x, y, z + 1, 'b+') # OK
T = np.arange(-np.pi, np.pi, np.pi/8)
X, Y = np.meshgrid(T, T)
Z = np.cos(X) * np.sin(Y)
wire = ax.plot_wireframe(X, Y, Z, linewidth=1) # OK
ax.contour(X, Y, Z + 5, offset=0) # OK (no effect offset ?)
surf = ax.plot_surface(X, Y, Z, linewidth=0) # OK
surf = ax.plot_surface(X, Y, Z, linewidth=0, color='red') # OK
surf = ax.plot_surface(X, Y, Z, linewidth=0, antialiased=True) # OK
fig.colorbar(surf) # error: must first set_array for mappable (need cmap ?)
                                cmap='bwr' # error: not callable self.cmap()
                                cmap=plt.cm.coolwarm # no attribute 'coolwarm'
surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.get_cmap(), linewidth=0) # OK
fig.colorbar(surf) # OK
------------------------------------------------------------------------
(new) py 3.x
# ax = fig.gca(projection='3d')
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect((1, 1, 1)) # (must be matplotlib >= 3.3)
surf = ax.plot_surface(X, Y, Z, linewidth=0, rcount=4, ccount=4)
surf = ax.plot_surface(X, Y, Z, cmap='bwr', linewidth=0)
fig.colorbar(surf)
------------------------------------------------------------------------
GeoGebra vertical-Y https://www.geogebra.org/m/acjx4ten
 ApplyMatrix https://wiki.geogebra.org/en/ApplyMatrix_Command
  error?: ApplyMatrix(M, (cos(t), sin(t), zeros, ones))
 Concentric circles
  O = Sequence(Curve(n cos(t), n sin(t), n / 2, t, -pi, pi), n, 1, 2, 0.2)
p = 0 <-pi, pi, pi / 64>
q = Sequence(t + p, t, -pi, pi, pi / 16)
e = Sequence(1, t, -pi, pi, pi / 16)
d = Sequence(0, t, -pi, pi, pi / 16)
r = e * pi / 6 # Sequence(pi / 6, t, -pi, pi, pi / 16)
A = {{e,d,d,d}, {d,cos(q),-sin(q),d}, {d,sin(q),cos(q),d}, {d,d,d,e}}
B = {{e,d,d,d}, {d,e,d,2 cos(q)}, {d,d,e,2 sin(q)}, {d,d,d,e}}
C = {{cos(r),d,sin(r),d}, {d,e,d,d}, {-sin(r),d,cos(r),d}, {d,d,d,e}}
M = C*B*A
R = Sequence(Curve(
  M(1,1,n)*cos(t)/2+M(1,2,n)*sin(t)/2+M(1,3,n)*0+M(1,4,n),
  M(2,1,n)*cos(t)/2+M(2,2,n)*sin(t)/2+M(2,3,n)*0+M(2,4,n),
  M(3,1,n)*cos(t)/2+M(3,2,n)*sin(t)/2+M(3,3,n)*0+M(3,4,n),
  t, -pi, pi), n, 1, 33)
R = Sequence(Curve(M(1, 1, n) cos(t) / 2 + M(1, 2, n) sin(t) / 2 + M(1, 3, n) * 0 + M(1, 4, n), M(2, 1, n) cos(t) / 2 + M(2, 2, n) sin(t) / 2 + M(2, 3, n) * 0 + M(2, 4, n), M(3, 1, n) cos(t) / 2 + M(3, 2, n) sin(t) / 2 + M(3, 3, n) * 0 + M(3, 4, n), t, -pi, pi), n, 1, 33)
------------------------------------------------------------------------
// draw 32 / 33 clircles ( 1 skipped )
for(i=0; i<8; ++i){
  ggbApplet.evalCommand('P_' + i + ' = Sequence(Curve(M(1, 1, n) cos(t) + M(1, 2, n) sin(t) + M(1, 3, n) * 0 + M(1, 4, n), M(2, 1, n) cos(t) + M(2, 2, n) sin(t) + M(2, 3, n) * 0 + M(2, 4, n), M(3, 1, n) cos(t) + M(3, 2, n) sin(t) + M(3, 3, n) * 0 + M(3, 4, n), t, -pi, pi), n, ' + (1 + i*4) + ', ' + (4 + i*4) + ')');
}
------------------------------------------------------------------------
o = ggbApplet.getAllObjectNames();
s = '';
o.forEach(p => s += (p + '-'));
ggbApplet.evalCommand('txt = Text("' + s + '")');
------------------------------------------------------------------------
e = ggbApplet.getXML('R'); // ggbApplet.debug(e);
f = ''; // [].forEach.call(e, p => f += ('00'+p.toString(16)).slice(-2));
for(i=0; i<e.length; ++i) f += ('00'+e.charCodeAt(i).toString(16)).slice(-2);
ggbApplet.evalCommand('txt = Text("'+f+'")');
------------------------------------------------------------------------
txt = Text("3c656c656d656e7420747970653d226c69737422206c6162656c3d2252223e0a093c73686f77206f626a6563743d227472756522206c6162656c3d2266616c7365222065763d2234222f3e0a093c6f626a436f6c6f7220723d223235352220673d22302220623d223235352220616c7068613d2230222064796e616d6963723d222870202b20c029202f20282832202a20c02929222064796e616d6963673d22302e38222064796e616d6963623d22302e382220636f6c6f7253706163653d2231222f3e0a093c6c617965722076616c3d2230222f3e0a093c6c6162656c4d6f64652076616c3d2230222f3e0a093c6c696e655374796c6520746869636b6e6573733d22322220747970653d223022207479706548696464656e3d2231222f3e0a093c706f696e7453697a652076616c3d2235222f3e0a093c706f696e745374796c652076616c3d2230222f3e0a093c616e676c655374796c652076616c3d2230222f3e0a3c2f656c656d656e743e0a")
------------------------------------------------------------------------
# binascii.a2b_hex('...')
------------------------------------------------------------------------
<element type="list" label="R">\n\t<show object="true" label="false" ev="4"/>\n\t<objColor r="255" g="0" b="255" alpha="0" dynamicr="(p + \xc0) / ((2 * \xc0))" dynamicg="0.8" dynamicb="0.8" colorSpace="1"/>\n\t<layer val="0"/>\n\t<labelMode val="0"/>\n\t<lineStyle thickness="2" type="0" typeHidden="1"/>\n\t<pointSize val="5"/>\n\t<pointStyle val="0"/>\n\t<angleStyle val="0"/>\n</element>\n
------------------------------------------------------------------------
<element type="list" label="R">
  <show object="true" label="false" ev="4"/>
  <objColor r="255" g="0" b="255" alpha="0" dynamicr="(p + \xc0) / ((2 * \xc0))" dynamicg="0.8" dynamicb="0.8" colorSpace="1"/>
  <layer val="0"/>
  <labelMode val="0"/>
  <lineStyle thickness="2" type="0" typeHidden="1"/>
  <pointSize val="5"/>
  <pointStyle val="0"/>
  <angleStyle val="0"/>
</element>
------------------------------------------------------------------------
js
  for(var i=0; i<10; ++i)
    ggbApplet.evalCommand("A_"+i+"=(random()*10,random()*10)");
slider
  script=If[b > 1.25, {"UpdateConstruction[]"}, {"c=3"}] https://help.geogebra.org/topic/slider-and-script
  script=If[b > 1.25, {"ZoomIn[1]"}, {"c=3"}] Since next release script=If[b > 1.25, {"ZoomIn[1]"}] will be sufficient.
  a=slider[1,3,1]
  list1 = {"red", "green", "blue"}
  On Update SetColor(a, Element(list1, a))
global
  function onAdd(name){ alert("Object "+name+" was added."); }
  function ggbOnInit(){ ggbApplet.registerAddListener("onAdd"); }
tutorial
  https://wiki.geogebra.org/en/Tutorial:Introduction_to_GeoGebraScript
  https://wiki.geogebra.org/en/Scripting_Commands
  SetLineThickness[a, Distance[A, a]*2]
  SetPointSize[A, Distance[A,y=0]]
  inc/dec button steps SetValue[Steps,Steps+1]
'''

import sys, os
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import hsv_to_rgb

def getHSV2RGB(h, s, v):
  hsv = (h / (2 * np.pi), s, v)
  # im = np.array([np.array([np.array(hsv)])]) # ok
  im = np.array([[hsv]]) # ok
  return (hsv_to_rgb(im)[0][0] * np.array([255, 255, 255])).astype(np.uint8)

def getColStr(r, g, b):
  return '#%02x%02x%02x' % (r, g, b)

def test_GeoGebra_InfiniteTube():
  fig = plt.figure(figsize=(6, 4), dpi=96)
  # ax = fig.add_subplot(111, projection='3d')
  ax = Axes3D(fig)
  ax.set_aspect('equal')

  x, y, z = [np.array(_) for _ in ([1,1,0,3,9], [1,4,5,6,9], [1,7,8,9,9])]
  ax.plot(x, y, z, 'g') # 3d line or curve
  ax.scatter(x, y, z - 1, 'rx') # OK 3d scatter
  ax.scatter3D(x, y, z + 1, 'b+') # OK

  r = np.pi / 6
  p = np.arange(-np.pi, np.pi, np.pi / 16)
  t = np.arange(-np.pi, np.pi, np.pi / 64)
  l = len(t)
  zeros = np.zeros(l)
  ones = np.ones(l)
  for q in p:
    rotx = np.array([
      [1, 0, 0, 0],
      [0, np.cos(q), -np.sin(q), 0],
      [0, np.sin(q), np.cos(q), 0],
      [0, 0, 0, 1]])
    tfyz = np.array([
      [1, 0, 0, 0],
      [0, 1, 0, 2 * np.cos(q)],
      [0, 0, 1, 2 * np.sin(q)],
      [0, 0, 0, 1]])
    roty = np.array([
      [np.cos(r), 0, np.sin(r), 0],
      [0, 1, 0, 0],
      [-np.sin(r), 0, np.cos(r), 0],
      [0, 0, 0, 1]])
    m = np.dot(roty, np.dot(tfyz, rotx))
    x, y, z, _ = np.dot(m, np.array([np.cos(t), np.sin(t), zeros, ones]))
    ax.plot(5 + x, 2 + y, 1 + z, getColStr(*getHSV2RGB(q + np.pi, 0.8, 0.8)))

  T = np.arange(-np.pi, np.pi, np.pi/8)
  X, Y = np.meshgrid(T, T)
  Z = np.cos(X) * np.sin(Y)
  wire = ax.plot_wireframe(X, Y, Z, linewidth=1) # OK
  ax.contour(X, Y, Z + 5, offset=0) # OK

  # surf = ax.plot_surface(X, Y, Z, linewidth=0) # OK
  # surf = ax.plot_surface(X, Y, Z, linewidth=0, color='red') # OK
  # surf = ax.plot_surface(X, Y, Z, linewidth=0, antialiased=True) # OK
  # surf = ax.plot_surface(X, Y, Z, cmap='bwr', linewidth=0)
  # surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.coolwarm, linewidth=0)
  surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.get_cmap(), linewidth=0) # OK
  # fig.colorbar(surf) # OK
  fig.colorbar(surf, shrink=0.5, aspect=10)

  plt.show()

if __name__ == '__main__':
  test_GeoGebra_InfiniteTube()
