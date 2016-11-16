# searchableSurfaceWithGaps 
## Class
Foam::searchableSurfaceWithGaps

## Description
searchableSurface using multiple slightly shifted underlying surfaces
to make sure pierces don't go through gaps:
- shift test vector with two small vectors (of size gap_) perpendicular
      to the original.
      Test with + and - this vector. Only if both register a hit is it seen
      as one.
- extend the test vector slightly (with SMALL) to account for numerical
      inaccuracies.

## SourceFiles
searchableSurfaceWithGaps.C

