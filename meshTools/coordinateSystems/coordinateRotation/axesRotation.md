# axesRotation 
## Class
Foam::axesRotation

## Description
A coordinate rotation specified using global axis

The rotation is defined by a combination of vectors (e1/e2), (e2/e3)
or (e3/e1). Any nonorthogonality will be absorbed into the second
vector.

```
axesRotation
{
        type        axesRotation;
        e1          (1 0 0);
        e2          (0 1 0);
}
```

## SourceFiles
axesRotation.C

