# activeBaffleVelocityFvPatchVectorField 
## Class
Foam::activeBaffleVelocityFvPatchVectorField

## Group
grpCoupledBoundaryConditions

## Description
This velocity boundary condition simulates the opening of a baffle due
to local flow conditions, by merging the behaviours of wall and cyclic
conditions.  The baffle joins two mesh regions, where the open fraction
determines the interpolation weights applied to each cyclic- and
neighbour-patch contribution.

We determine whether the baffle is opening or closing from the sign of
the net force across the baffle, from which the baffle open fraction is
updated using:

        \f[
            x = x_{old} + sign(F_{net})\frac{dt}{DT}
        \f]

where

\vartable
        x       | baffle open fraction [0-1]
        x_{old} | baffle open fraction on previous evaluation
        dt      | simulation time step
        DT      | time taken to open the baffle
        F_{net} | net force across the baffle
\endvartable

The open fraction is then applied to scale the patch areas.

## Usage

        Property     | Description             | Required    | Default value
        p            | pressure field name     | no          | p
        cyclicPatch  | cylclic patch name      | yes         |
        orientation  | 1 or -1 used to switch flow direction | yes|
        openFraction | current opatch open fraction [0-1]| yes |
        openingTime  | time taken to open the baffle | yes |
        maxOpenFractionDelta | max open fraction change per timestep | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            activeBaffleVelocity;
        p               p;
        cyclicPatch     cyclic1;
        orientation     1;
        openFraction    0.2;
        openingTime     5.0;
        maxOpenFractionDelta 0.1;
}
```

## See also
Foam::fixedValueFvPatchField
Foam::cyclicFvPatchField

## SourceFiles
activeBaffleVelocityFvPatchVectorField.C

