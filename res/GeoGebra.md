GeoGebra
========

一覧
 - [色相環(HSV)Color](https://www.geogebra.org/m/hysdcz29)
 - [フーリエ級数(めりくり)](https://www.geogebra.org/m/ccbru6zw)
 - [フーリエ級数とリサージュ図形(X-Y)](https://www.geogebra.org/m/q5ezvbdn)
 - [リサージュ図形(あけおめ)](https://www.geogebra.org/m/wdj2tbap)
 - [軌跡(ぐるぐる定規)Spirograph](https://www.geogebra.org/m/ueesvwyu)
 - [軌跡(ぐるぐる定規)Spirograph(全機能版)](https://www.geogebra.org/m/wevkfgev)
 - [Infinite Tube](https://www.geogebra.org/m/acjx4ten)
 - [Golden Ratio (scripting)](https://www.geogebra.org/m/mrfk9vaf)
 - [C60 Fullerene (scripting)](https://www.geogebra.org/m/rfbr2awx)
 - [接弦定理の直観的理解](https://www.geogebra.org/m/dpshmmu4)
 - [フーリエ級数とリサージュ図形(3D版)](https://www.geogebra.org/m/fznjbmcu)

手順
 - [色相環(HSV)Color](https://www.geogebra.org/m/hysdcz29)
```plain.txt
作図 画像 img = アップロード
自由 A = (-4, 2) # (非表示) 画像 左下
自由 B = (-1, 2) # (非表示) 画像 右下
t=2π (上級 HSV H=t/(2π) S=1 V=1)
# th = Sequence(i, i, 0, t, 0.01) # (非表示)
u = -2cos(t) # -2cos(th)
v = 2sin(t) # 2sin(th)
作図 点 C = (u, v) # H=th/(2π)だと失敗？ (上級 HSV H=t/(2π) S=1 V=1) 残像 on 点サイズ 8 点スタイル 縁無 サイズ 60
    (点毎の色が変えられない全部の点の色が変わる？ th = Sequence(i, i, 0, t, 0.01) が原因 解決)
作図 ボタン btn_redraw # cindyscript {t=0;} 背景 gray (濃) (上級 HSV H=t/(2π) S=1 V=1) 前景色のみ可変？
作図 画像 out = アップロード
自由 D = (1, 2) # (非表示) 画像 左下
自由 E = (4, 2) # (非表示) 画像 右下
```

 - [フーリエ級数(めりくり)](https://www.geogebra.org/m/ccbru6zw)
```plain.txt
t=2π (青) 増分 0.000001 速度 3 増加のみ 繰り返し
d={{...},{...},{...},{...}} # (緑) 固定値 転置 63個
th = Sequence(-(i-3) t, i, 3, 65) # (非表示) d の個数と合わせる
u = Sum(d(1)cos(th) + d(2)sin(th)) # (非表示)
v = -Sum(d(3)cos(th) + d(4)sin(th)) # (非表示)
作図 点 P (u, v) # (薄緑 -> 上級 HSV H=c S=1 V=1) 残像 on
範囲 x: -400 <-> 0 y: -200 <-> 310 (適当)
c = if(t < 1.2, 0.78, if(t > 4, 0, 1.77)) / (2π)
```

 - [フーリエ級数とリサージュ図形(X-Y)](https://www.geogebra.org/m/q5ezvbdn)
```plain.txt
t=2π (薄橙) 増分 0.01 速度 1.2 振動 繰り返し
a1, a2, a3 = 1/1, 1/2, 1/3 (青) スライダー 0 <-> 1
b1, b2, b3 = 1/3, 1/4, 1/2 (桃) スライダー 0 <-> 1
(Σa[n]cos(nt), Σb[n]sin(nt))
d = {{...},{...}} # (緑) (a1, a2, a3, b1, b2, b3 を表に代入) 転置 3個
th = Sequence(i t, i, 1, 3) # (非表示) d の個数と合わせる
u = 10Sum(d(1)cos(th))
v = 10Sum(d(2)sin(th))
s = -35 + 2t
作図 点 A (u, s) # (薄青) 直線(単に確認用)
作図 点 B (s, v) # (薄桃) 直線(単に確認用)
C = Curve(20cos(th), 20sin(th), th, 0, t) # (薄橙) Sequence の th とは無関係 ただし t と同期
作図 点 F (u, v) # (薄緑) 残像 on
G = Segment((u, s), (u, v)) # (薄cyan) 細線2
H = Segment((s, v), (u, v)) # (薄赤) 細線2
範囲 x: -20 <-> 30 y: -40 <-> 40 (適当)
```

 - [リサージュ図形(あけおめ)](https://www.geogebra.org/m/wdj2tbap)
```plain.txt
t=2π (青) 増分 0.000001 速度 3 増加のみ 繰り返し
d={{...},{...},{...},{...}} # (緑) 固定値 転置 63個
th = Sequence(-(i-3) t, i, 3, 65) # (非表示) d の個数と合わせる
u = Sum(d(1)cos(th) + d(2)sin(th)) # (非表示)
v = Sum(d(3)cos(th) + d(4)sin(th)) # (非表示)
作図 点 P (u, v) # (薄緑 -> 上級 HSV H=3t/(2π) S=1 V=1) 残像 on
範囲 x: -400 <-> 0 y: -200 <-> 310 (適当)
```

 - [軌跡(ぐるぐる定規)Spirograph](https://www.geogebra.org/m/ueesvwyu)
 - [軌跡(ぐるぐる定規)Spirograph(全機能版)](https://www.geogebra.org/m/wevkfgev)
```plain.txt
 # Qx = (r-q)cos(t), Qy = (r-q)sin(t)
 # Px = Qx + (q-p)cos((1-r/q)t), Py = Qy + (q-p)sin((1-r/q)t)
 p, q, r = 2, 3, 5
 p, q, r = 7, 11, 15
 p, q, r = 7, 11, 23
 p, q, r = 5, 17, 23
 th=60π (θ slider 最小 0 最大 60π)
 Curve((r-q)cos(t) + (q-p)cos((1-r/q)t), (r-q)sin(t) + (q-p)sin((1-r/q)t), t, 0, th)
 Curve((r-q)cos(th) + q cos(t), (r-q)sin(th) + q sin(t), t, 0, 2π)
 Curve(r cos(t), r sin(t), t, 0, 2π)
 Line(((r-q)cos(th), (r-q)sin(th)), ((r-q)cos(th) + (q-p)cos((1-r/q)th), (r-q)sin(th) + (q-p)sin((1-r/q)th)))
```

 - [twitter](https://twitter.com/nomissbowling/status/1012650562125324290)
