# fixedProfileFvPatchField 
## Class
Foam::fixedProfileFvPatchField

## Group
grpGenericBoundaryConditions

## Description
This boundary condition provides a fixed value profile condition.

## Usage

        Property     | Description              | Required | Default value
        profile      | Profile Function1        | yes |
        direction    | Profile direction        | yes |
        origin       | Profile origin           | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            fixedProfile;
        profile    csvFile;

        profileCoeffs
        {
            nHeaderLine         0;          // Number of header lines
            refColumn           0;          // Reference column index
            componentColumns    (1 2 3);    // Component column indices
            separator           ",";        // Optional (defaults to ",")
            mergeSeparators     no;         // Merge multiple separators
            fileName            "Uprofile.csv";  // name of csv data file
            outOfBounds         clamp;      // Optional out-of-bounds handling
            interpolationScheme linear;     // Optional interpolation scheme
        }
        direction        (0 1 0);
        origin           0;
}
```

Example setting a parabolic inlet profile for the PitzDaily case:
```
inlet
{
        type            fixedProfile;

        profile         polynomial
        (
            ((1 0 0)        (0 0 0))
            ((-6200 0 0)    (2 0 0))
        );
        direction       (0 1 0);
        origin          0.0127;
}
```

## Note
The profile entry is a Function1 type.  The example above gives the
usage for supplying csv file.

## See also
Foam::fixedValueFvPatchField
Foam::Function1Types
Foam::timeVaryingMappedFixedValueFvPatchField

## SourceFiles
fixedProfileFvPatchField.C

