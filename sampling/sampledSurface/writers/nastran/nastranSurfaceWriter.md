# nastranSurfaceWriter 
## Class
Foam::nastranSurfaceWriter

## Description
A surface writer for the Nastran file format - both surface mesh and fields

formatOptions
{
        nastran
        {
            // From OpenFOAM field name to Nastran field name
            fields ((pMean PLOAD2));
            // Optional scale
            scale 2.0;
            // Optional format
            format free;    //short, long, free
        }
};

## SourceFiles
nastranSurfaceWriter.C
nastranSurfaceWriterTemplates.C

