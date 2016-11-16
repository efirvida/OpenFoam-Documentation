# mappedFlowRateFvPatchVectorField 
## Class
Foam::mappedFlowRateFvPatchVectorField

## Group
grpInletBoundaryConditions grpCoupledBoundaryConditions

## Description
Describes a volumetric/mass flow normal vector boundary condition by its
magnitude as an integral over its area.

The inlet mass flux is taken from the neighbour region.

The basis of the patch (volumetric or mass) is determined by the
dimensions of the flux, phi.  The current density is used to correct the
velocity when applying the mass basis.

## Usage

        Property     | Description             | Required    | Default value
        phi          | flux field name         | no          | phi
        rho          | density field name      | no          | rho
        neigPhi      | name of flux field on neighbour mesh | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            mappedFlowRate;
        phi             phi;
        rho             rho;
        neigPhi         phi;
        value           uniform (0 0 0); // placeholder
}
```

## SourceFiles
mappedFlowRateFvPatchVectorField.C

