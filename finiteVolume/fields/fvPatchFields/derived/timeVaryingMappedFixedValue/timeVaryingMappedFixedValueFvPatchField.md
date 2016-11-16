# timeVaryingMappedFixedValueFvPatchField 
## Class
Foam::timeVaryingMappedFixedValueFvPatchField

## Group
grpInletBoundaryConditions grpCoupledBoundaryConditions

## Description
This boundary conditions interpolates the values from a set of supplied
points in space and time.  Supplied data should be specified in
constant/boundaryData/\<patchname\> where:
- points : pointField with locations
- ddd: supplied values at time ddd
The default mode of operation (mapMethod planarInterpolation) is
to project the points onto a plane (constructed from the first threee
points) and construct a 2D triangulation and finds for the face centres
the triangle it is in and the weights to the 3 vertices.

The optional mapMethod nearest will avoid all projection and
triangulation and just use the value at the nearest vertex.

Values are interpolated linearly between times.

## Usage

        Property     | Description             | Required    | Default value
        setAverage   | flag to activate setting of average value | yes |
        perturb      | perturb points for regular geometries | no | 1e-5
        fieldTableName | alternative field name to sample | no| this field name
        mapMethod    | type of mapping | no | planarInterpolation
        offset   | for applying offset to mapped values  | no | constant 0.0


```
<patchName>
{
        type            timeVaryingMappedFixedValue;
        setAverage      false;
        //perturb       0.0;
        //fieldTableName samples;
        //offset    constant 0.2;
}
```

## See also
Foam::fixedValueFvPatchField
Foam::Function1Types

## SourceFiles
timeVaryingMappedFixedValueFvPatchField.C

