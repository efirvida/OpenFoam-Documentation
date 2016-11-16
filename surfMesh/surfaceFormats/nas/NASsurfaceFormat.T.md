# NASsurfaceFormat.T 
## Class
Foam::fileFormats::NASsurfaceFormat

## Description
Nastran surface reader.

- Uses the Ansa "$ANSA_NAME" or the Hypermesh "$HMNAME COMP" extensions
      to obtain zone names.
- Handles Nastran short and long formats, but not free format.
- Properly handles the Nastran compact floating point notation: \n
```
        GRID          28        10.20269-.030265-2.358-8
```

## SourceFiles
NASsurfaceFormat.C

