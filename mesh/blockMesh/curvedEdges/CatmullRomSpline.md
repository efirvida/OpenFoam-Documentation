# CatmullRomSpline 
## Class
Foam::CatmullRomSpline

## Description
An implementation of Catmull-Rom splines
(sometimes known as Overhauser splines).

In this implementation, the end tangents are created automatically
by reflection.

In matrix form, the \e local interpolation on the interval t=[0..1] is
described as follows:
```
P(t) = 1/2 * [ t^3 t^2 t 1 ] * [ -1  3 -3  1 ] * [ P-1 ]
                                   [  2 -5  4 -1 ]   [ P0 ]
                                   [ -1  0  1  0 ]   [ P1 ]
                                   [  0  2  0  0 ]   [ P2 ]
```

Where P-1 and P2 represent the neighbouring points or the extrapolated
end points. Simple reflection is used to automatically create the end
points.

The spline is discretized based on the chord length of the individual
segments. In rare cases (sections with very high curvatures), the
resulting distribution may be sub-optimal.

A future implementation could also handle closed splines.

## See also
http://www.algorithmist.net/catmullrom.html provides a nice
introduction

## SourceFiles
CatmullRomSpline.C

