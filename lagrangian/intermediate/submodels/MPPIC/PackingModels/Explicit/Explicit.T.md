# Explicit.T 
## Class
Foam::PackingModels::Explicit

## Description
Explicit model for applying an inter-particle stress to the particles.

The inter-particle stress is calculated using current particle locations.
This force is then applied only to the particles that are moving towards
regions of close pack. The resulting velocity change is limited using an
abtracted correction velocity limiter.

Reference:
```
        "An Incompressible Three-Dimensional Multiphase Particle-in-Cell Model
        for Dense Particle Flows"
        D Snider
        Journal of Computational Physics
        Volume 170, Issue 2, Pages 523-549, July 2001
```

## SourceFiles
Explicit.C

