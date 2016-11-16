# wallBoundedStreamLine 
## Class
Foam::functionObjects::wallBoundedStreamLine

## Group
grpFieldFunctionObjects

## Description
This function object generates streamline data by sampling a set of
user-specified fields along a particle track, transported by a
user-specified velocity field, constrained to a patch.

Example of function object specification:
```
wallBoundedStreamLine1
{
        type            wallBoundedStreamLine;
        libs ("libfieldFunctionObjects.so");
        ...
        setFormat       vtk;
        U               UNear;
        trackForward    yes;
        fields
        (
            UNear
            p
        );
        lifeTime        10000;
        trackLength     1e-3;
        nSubCycle       5;
        cloudName       particleTracks;
        seedSampleSet   patchSeed;
        patchSeedCoeffs
        {
            type        patchSeed;
            patches     (wall);
            axis        x;
            maxPoints   20000;
        }
}
```

## Usage

        Property     | Description             | Required    | Default value
        type         | Type name: wallBoundedStreamLine| yes |
        setFormat    | Output data type        | yes         |
        U            | Tracking velocity field name | yes    |
        fields       | Fields to sample        | yes         |
        lifetime     | Maximum number of particle tracking steps | yes |
        trackLength  | Tracking segment length | no          |
        nSubCycle    | Number of tracking steps per cell | no|
        cloudName    | Cloud name to use       | yes         |
        seedSampleSet| Seeding method (see below)| yes       |


Where \c seedSampleSet is typically one of
\plaintable
        uniform | uniform particle seeding
        cloud   | cloud of points
        patchSeed | seeding via patch faces
        triSurfaceMeshPointSet | points according to a tri-surface mesh
\endplaintable

## Note
When specifying the track resolution, the \c trackLength OR \c nSubCycle
option should be used

## See also
Foam::functionObject
Foam::functionObjects::timeControl
Foam::sampledSet
Foam::streamLine

## SourceFiles
wallBoundedStreamLine.C

