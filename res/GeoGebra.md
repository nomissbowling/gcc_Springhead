GeoGebra
========

一覧
 - [色相環(HSV)Color](https://www.geogebra.org/m/hysdcz29)
 - [フーリエ級数(めりくり)](https://www.geogebra.org/m/ccbru6zw)
 - [フーリエ級数とリサージュ図形(X-Y)](https://www.geogebra.org/m/q5ezvbdn)
 - [リサージュ図形(あけおめ)](https://www.geogebra.org/m/wdj2tbap)
 - [軌跡(ぐるぐる定規)Spirograph](https://www.geogebra.org/m/ueesvwyu)
 - [軌跡(ぐるぐる定規)Spirograph(全機能版)](https://www.geogebra.org/m/wevkfgev)

手順
 - [色相環(HSV)Color](https://www.geogebra.org/m/hysdcz29)
 - [フーリエ級数(めりくり)](https://www.geogebra.org/m/ccbru6zw)
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
 - [軌跡(ぐるぐる定規)Spirograph](https://www.geogebra.org/m/ueesvwyu)
 - [軌跡(ぐるぐる定規)Spirograph(全機能版)](https://www.geogebra.org/m/wevkfgev)
