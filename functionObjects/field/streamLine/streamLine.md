# streamLine 
## Class
Foam::functionObjects::streamLine

## Group
grpFieldFunctionObjects

## Description
This function object generates streamline data by sampling a set of
user-specified fields along a particle track, transported by a
user-specified velocity field.

Example of function object specification:
```
streamLine1
{
        type            streamLine;
        libs ("libfieldFunctionObjects.so");
        ...
        setFormat       vtk;
        trackForward    yes;
        fields
        (
            U
            p
        );
        lifeTime        10000;
        trackLength     1e-3;
        nSubCycle       5;
        cloudName       particleTracks;
        seedSampleSet   uniform;
        uniformCoeffs
        {
            type        uniform;
            axis        x;  //distance;
            start       (-0.0205 0.0001 0.00001);
            end         (-0.0205 0.0005 0.00001);
            nPoints     100;
        }
}
```

## Usage

        Property     | Description             | Required    | Default value
        type         | Type name: streamLine   | yes         |
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
        triSurfaceMeshPointSet | points according to a tri-surface mesh
\endplaintable

## Note
When specifying the track resolution, the \c trackLength OR \c nSubCycle
option should be used

## See also
Foam::functionObject
Foam::functionObjects::timeControl
Foam::sampledSet
Foam::wallBoundedStreamLine

## SourceFiles
streamLine.C

