# coordinateSystems 
## Class
Foam::coordinateSystems

## Description
Provides a centralized coordinateSystem collection.

## Note
Mixing normal constructors and the coordinateSystems::New constructor
may yield unexpected results.

```
        1
        (
        cat1
        {
            coordinateSystem  system_10;
            porosity        0.781;
            Darcy
            {
                d   d [0 -2 0 0 0]  (-1000 -1000 0.50753e+08);
                f   f [0 -1 0 0 0]  (-1000 -1000 12.83);
            }
        }
        )
```

For this to work correctly, the coordinateSystem constructor must be
supplied with both a dictionary and an objectRegistry.

## SourceFiles
coordinateSystems.C

