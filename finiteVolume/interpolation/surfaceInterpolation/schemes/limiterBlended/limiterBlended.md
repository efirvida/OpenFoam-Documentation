# limiterBlended 
## Class
Foam::limiterBlended

## Description
Blends two specified schemes using the limiter function provided by a
limitedSurfaceInterpolationScheme.

The limited scheme is specified first followed by the scheme to be scaled
by the limiter and then the scheme scaled by 1 - limiter e.g.

    div(phi,U)      Gauss limiterBlended vanLeer linear linearUpwind grad(U);

## SourceFiles
limiterBlended.C

