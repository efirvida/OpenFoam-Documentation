# wallPointYPlus 
## Class
Foam::wallPointYPlus

## Description
Holds information (coordinate and yStar) regarding nearest wall point.

Used in VanDriest wall damping where the interest is in y+ but only
needs to be calculated up to e.g. y+ < 200. In all other cells/faces
the damping function becomes 1, since y gets initialized to GREAT and
yStar to 1.

Note: should feed the additional argument (yPlusCutoff) through as a
template argument into FaceCellWave

## SourceFiles
wallPointYPlusI.H
wallPointYPlus.C

