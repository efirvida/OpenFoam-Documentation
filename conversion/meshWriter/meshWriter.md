# meshWriter 
## Class
Foam::meshWriter

## Description
write OpenFOAM meshes and/or results to another CFD format
- currently just STAR-CD

## \par Files

"constant/boundaryRegion" is an IOMap<dictionary> that contains
the boundary type and names. eg,
```
        (
            0
            {
                BoundaryType    wall;
                Label           Default_Boundary_Region;
            }

            1
            {
                BoundaryType    inlet;
                Label           inlet_1;
            }

            ...

            4
            {
                BoundaryType    pressure;
                Label           outlet;
            }
        )
```


## SourceFiles
meshWriterI.H
meshWriter.C
meshWriterIO.C

