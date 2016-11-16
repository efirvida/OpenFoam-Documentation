# nutWallFunctionFvPatchScalarField 
## Class
Foam::nutWallFunctionFvPatchScalarField

## Group
grpWallFunctions

## Description
This boundary condition provides a turbulent kinematic viscosity condition
when using wall functions, based on turbulence kinetic energy.
- replicates OpenFOAM v1.5 (and earlier) behaviour

## Usage

        Property  | Description         | Required   | Default value
        Cmu       | Cmu coefficient     | no         | 0.09
        kappa     | Von Karman constant | no         | 0.41
        E         | E coefficient       | no         | 9.8


Examples of the boundary condition specification:
```
<patchName>
{
        type            nutWallFunction;
        value           uniform 0.0;
}
```

Reference for the default model coefficients:
```
        H. Versteeg, W. Malalasekera
        An Introduction to Computational Fluid Dynamics: The Finite Volume
        Method, subsection "3.5.2 k-epsilon model"
```

## See also
Foam::fixedValueFvPatchField

## SourceFiles
nutWallFunctionFvPatchScalarField.C

