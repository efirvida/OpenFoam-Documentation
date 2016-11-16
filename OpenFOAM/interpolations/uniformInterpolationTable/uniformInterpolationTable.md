# uniformInterpolationTable 
## Class
Foam::uniformInterpolationTable

## Description
Table with uniform interval in independant variable, with linear
interpolation

Example usage (scalar): values specified within a dictionary:

```
{
        x0          0;          // lower limit
        dx          0.2;        // fixed interval
        log10       true;       // take log(10) when interpolating?
        data                    // list of dependent data values
        (
            7870                // value at x0
            7870                // value at x0 + dx
            ...
            7870                // value at x0 + n*dx
        );
}
```

## SourceFiles
uniformInterpolationTable.C

