# activePressureForceBaffleVelocityFvPatchVectorField 
## Class
Foam::activePressureForceBaffleVelocityFvPatchVectorField

## Group
grpCoupledBoundaryConditions

## Description
This boundary condition is applied to the flow velocity, to simulate the
opening or closure of a baffle due to local pressure or force changes,
by merging the behaviours of wall and cyclic conditions.

The baffle joins two mesh regions, where the open fraction determines
the interpolation weights applied to each cyclic- and neighbour-patch
contribution. This means that this is boundary condition is meant to be
used in an extra wall beyond an existing cyclic patch pair. See PDRMesh
for more details.

Once the threshold is crossed, this condition activated and continues to
open or close at a fixed rate using

        \f[
            x = x_{old} + s \times \frac{dt}{DT}
        \f]

where

\vartable
        x       | baffle open fraction [0-1]
        x_{old} | baffle open fraction on previous evaluation
        s       | sign for orientation: 1 to open or -1 to close
        dt      | simulation time step
        DT      | time taken to open the baffle
\endvartable

The open fraction is then applied to scale the patch areas.

## Usage

        Property     | Description             | Required    | Default value
        p            | pressure field name     | no          | p
        cyclicPatch  | cyclic patch name       | yes         |
        orientation  | 1 to open or -1 to close | yes|
        openFraction | current open fraction [0-1] | yes |
        openingTime  | time taken to open or close the baffle | yes |
        maxOpenFractionDelta | max fraction change per timestep | yes |
        minThresholdValue | minimum absolute pressure or
                            force difference for activation | yes |
        forceBased   | force (true) or pressure-based (false) activation | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            activePressureForceBaffleVelocity;
        p               p;
        cyclicPatch     cyclic1;
        orientation     1;
        openFraction    0.2;
        openingTime     5.0;
        maxOpenFractionDelta 0.1;
        minThresholdValue 0.01;
        forceBased      false;
}
```

## SourceFiles
activePressureForceBaffleVelocityFvPatchVectorField.C

