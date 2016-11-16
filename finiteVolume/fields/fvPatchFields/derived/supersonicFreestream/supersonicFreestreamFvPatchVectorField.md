# supersonicFreestreamFvPatchVectorField 
## Class
Foam::supersonicFreestreamFvPatchVectorField

## Group
grpInletBoundaryConditions grpOutletBoundaryConditions

## Description
This boundary condition provides a supersonic free-stream condition.

- supersonic outflow is vented according to ???
- supersonic inflow is assumed to occur according to the Prandtl-Meyer
      expansion process.
- subsonic outflow is applied via a zero-gradient condition from inside
      the domain.

## Usage

        Property     | Description             | Required    | Default value
        T            | Temperature field name  | no          | T
        p            | Pressure field name     | no          | p
        psi          | Compressibility field name | no       | thermo:psi
        UInf         | free-stream velocity    | yes         |
        pInf         | free-stream pressure    | yes         |
        TInf         | free-stream temperature | yes         |
        gamma        | heat capacity ratio (cp/Cv) | yes     |


Example of the boundary condition specification:
```
<patchName>
{
        type            supersonicFreestream;
        UInf            500;
        pInf            1e4;
        TInf            265;
        gamma           1.4;
}
```

## Note
This boundary condition is ill-posed if the free-stream flow is normal
to the boundary.

## SourceFiles
supersonicFreestreamFvPatchVectorField.C

