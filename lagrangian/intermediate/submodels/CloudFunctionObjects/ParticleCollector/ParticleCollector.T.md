# ParticleCollector.T 
## Class
Foam::ParticleCollector

## Description
Function object to collect the parcel mass- and mass flow rate over a
set of polygons.  The polygons can either be specified by sets of user-
supplied points, or in a concentric circles arrangement.  If a
parcel is 'collected', it can be flagged to be removed from the
domain using the removeCollected entry.

Example usage:
```
particleCollector1
{
        type            particleCollector;

        mode            concentricCircle;
        origin          (0.05 0.025 0.005);
        radius          (0.01 0.025 0.05);
        nSector         10;
        refDir          (1 0 0);
        normal          (0 0 1);

        negateParcelsOppositeNormal no;
        removeCollected no;
        surfaceFormat   vtk;
        resetOnWrite    no;
        log             yes;
}

particleCollector2
{
        type            particleCollector;

        mode            polygon;
        polygons
        (
            (
                (0 0 0)
                (1 0 0)
                (1 1 0)
                (0 1 0)
            )
            (
                (0 0 1)
                (1 0 1)
                (1 1 1)
                (0 1 1)
            )
        );
        normal          (0 0 1);

        negateParcelsOppositeNormal no;
        removeCollected no;
        surfaceFormat   vtk;
        resetOnWrite    no;
        log             yes;
}
```

## SourceFiles
ParticleCollector.C

