# rotatedBoxToCell 
## Class
Foam::rotatedBoxToCell

## Description
A topoSetSource to select cells based on cell centres inside
rotated/skewed box (parallelopiped?).

Box defined as origin and i,j,k vectors.
E.g. box rotated 45 degrees around z-axis with sizes sqrt(0.2^2+0.2^2)
(and extra large, 200 in z direction):
```
       origin   ( 0.4 0.4 -100);
       i        ( 0.2 0.2    0);
       j        (-0.2 0.2    0);
       k        ( 0.0 0.0  100);
```

## SourceFiles
rotatedBoxToCell.C

