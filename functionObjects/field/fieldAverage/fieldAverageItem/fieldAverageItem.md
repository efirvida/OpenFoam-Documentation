# fieldAverageItem 
## Class
Foam::functionObjects::fieldAverageItem

## Description
Helper class to describe what form of averaging to apply.  A set will be
applied to each base field in Foam::fieldAverage, of the form:

```
{
        mean            on;
        prime2Mean      on;
        base            time; // iteration
        window          200;  // optional averaging window
        windowName      w1;   // optional window name (default = "")
}
```

The averaging window corresponds to the averaging interval (iters or time)
If not specified, the averaging is over 'all iters/time'

## SourceFiles
fieldAverageItem.C
fieldAverageItemIO.C

