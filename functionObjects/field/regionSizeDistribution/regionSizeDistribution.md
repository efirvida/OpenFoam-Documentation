# regionSizeDistribution 
## Class
Foam::functionObjects::regionSizeDistribution

## Group
grpFieldFunctionObjects

## Description
This function object creates a size distribution via interrogating a
continuous phase fraction field.

Looks up a phase-fraction (alpha) field and splits the mesh into regions
based on where the field is below the threshold value.  These
regions ("droplets") can now be analysed.

Regions:
- print the regions connected to a user-defined set of patches.
      (in spray calculation these form the liquid core)
- print the regions with too large volume.  These are the 'background'
      regions.
- (debug) write regions as a volScalarField
- (debug) print for all regions the sum of volume and alpha*volume

Output (volume scalar) fields include:
- alpha_liquidCore : alpha with outside liquid core set to 0
- alpha_background : alpha with outside background set to 0.

%Histogram:
- determine histogram of diameter (given minDiameter, maxDiameter, nBins)
- write graph of number of droplets per bin
- write graph of sum, average and deviation of droplet volume per bin
- write graph of sum, average and deviation of user-defined fields.  For
      volVectorFields these are those of the 3 components and the magnitude.

Example of function object specification:
```
regionSizeDistribution1
{
        type            regionSizeDistribution;
        libs ("libfieldFunctionObjects.so");
        ...
        field           alpha;
        patches         (inlet);
        threshold       0.4;
        fields          (p U);
        nBins           100;
        maxDiameter     0.5e-4;
        minDiameter     0;
        setFormat       gnuplot;
        coordinateSystem
        {
            type            cartesian;
            origin          (0 0 0);
            e3              (0 1 1);
            e1              (1 0 0);
        }
}
```

## Usage

        Property     | Description             | Required    | Default value
        type         | type name: regionSizeDistribution |yes|
        field        | phase field to interrogate | yes      |
        patches      | patches from which the liquid core is identified | yes|
        threshold    | phase fraction applied to delimit regions | yes |
        fields       | fields to sample        | yes         |
        nBins        | number of bins for histogram | yes    |
        maxDiameter  | maximum region equivalent diameter | yes |
        minDiameter  | minimum region equivalent diameter | no  | 0
        setFormat    | writing format          | yes         |
        coordinateSystem | transformation for vector fields | no         |


## See also
Foam::functionObject
Foam::functionObjects::writeFile

## SourceFiles
regionSizeDistribution.C

