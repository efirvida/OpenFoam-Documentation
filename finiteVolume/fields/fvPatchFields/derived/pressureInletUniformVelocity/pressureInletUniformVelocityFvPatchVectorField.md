# pressureInletUniformVelocityFvPatchVectorField 
## Class
Foam::pressureInletUniformVelocityFvPatchVectorField

## Group
grpInletBoundaryConditions

## Description
This velocity inlet boundary condition is applied to patches where the
pressure is specified.  The uniform inflow velocity is obtained by
averaging the flux over the patch, and then applying it in the direction
normal to the patch faces.

## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            pressureInletUniformVelocity;
        value           uniform 0;
}
```

## SourceFiles
pressureInletUniformVelocityFvPatchVectorField.C

