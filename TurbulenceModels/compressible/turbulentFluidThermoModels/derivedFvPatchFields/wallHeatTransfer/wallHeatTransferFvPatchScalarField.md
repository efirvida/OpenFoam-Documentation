# wallHeatTransferFvPatchScalarField 
## Class
Foam::wallHeatTransferFvPatchScalarField

## Group
grpThermoBoundaryConditions grpWallBoundaryConditions

## Description
This boundary condition provides an enthalpy condition for wall heat
transfer

## Usage

        Property     | Description             | Required    | Default value
        Tinf         | wall temperature        | yes         |
        alphaWall    | thermal diffusivity     | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            wallHeatTransfer;
        Tinf            uniform 500;
        alphaWall       uniform 1;
}
```

## SourceFiles
wallHeatTransferFvPatchScalarField.C

