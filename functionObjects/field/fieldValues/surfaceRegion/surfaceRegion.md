# surfaceRegion 
## Class
Foam::functionObjects::fieldValues::surfaceRegion

## Group
grpFieldFunctionObjects

## Description
This function object provides a 'face regionType' variant of the fieldValues
function object.  Given a list of user-specified fields and a selection
of mesh (or general surface) faces, a number of operations can be
performed, such as sums, averages and integrations.

For example, to calculate the volumetric or mass flux across a patch,
apply the 'sum' operator to the flux field (typically \c phi)

Example of function object specification:
```
surfaceRegion1
{
        type            surfaceRegion;
        libs ("libfieldFunctionObjects.so");
        ...
        log             yes;
        writeFields     true;
        surfaceFormat   none;
        regionType      faceZone;
        name            f0;
        operation       sum;
        weightField     alpha1;
        fields
        (
            p
            phi
            U
        );
}
```

## Usage

        Property     | Description             | Required    | Default value
        type         | type name: surfaceRegion   | yes         |
        log          | write data to standard output | no    | no
        writeFields  | Write the region field values  | yes     |
        writeArea    | Write the area of the surfaceRegion | no |
        surfaceFormat | output value format    | no          |
        regionType   | face regionType: see below  | yes         |
        name         | name of face regionType if required  | no |
        operation    | operation to perform    | yes         |
        weightField  | name of field to apply weighting | no |
        orientedWeightField  | name of oriented field to apply weighting | no |
        scaleFactor  | scale factor            | no          | 1
        fields       | list of fields to operate on | yes    |
        orientedFields | list of oriented fields to operate on | no |


Where \c regionType is defined by
\plaintable
        faceZone     | requires a 'name' entry to specify the faceZone
        patch        | requires a 'name' entry to specify the patch
        sampledSurface | requires a 'sampledSurfaceDict' sub-dictionary
\endplaintable

The \c operation is one of:
\plaintable
       none          | no operation
       sum           | sum
       sumMag        | sum of component magnitudes
       sumDirection  | sum values which are positive in given direction
       sumDirectionBalance | sum of balance of values in given direction
       average       | ensemble average
       weightedAverage | weighted average
       areaAverage   | area weighted average
       weightedAreaAverage | weighted area average
       areaIntegrate | area integral
       min           | minimum
       max           | maximum
       CoV           | coefficient of variation: standard deviation/mean
       areaNormalAverage| area weighted average in face normal direction
       areaNormalIntegrate | area weighted integral in face normal directon
\endplaintable

## Note
- The values reported by the areaNormalAverage and areaNormalIntegrate
      operations are written as the first component of a field with the same
      rank as the input field.
- faces on empty patches get ignored
- if the field is a volField the \c faceZone can only consist of boundary
      faces
- the `oriented' entries relate to mesh-oriented fields, such as the
      flux, phi.  These fields will be oriented according to the face normals.
- using \c sampledSurfaces:
        - not available for surface fields
        - if interpolate=true they use \c interpolationCellPoint
          otherwise they use cell values
        - each triangle in \c sampledSurface is logically only in one cell
          so interpolation will be wrong when triangles are larger than
          cells.  This can only happen for sampling on a \c triSurfaceMesh
        - take care when using isoSurfaces - these might have duplicate
          triangles and so integration might be wrong

## See also
Foam::fieldValues
Foam::functionObject

## SourceFiles
surfaceRegion.C
surfaceRegionTemplates.C

