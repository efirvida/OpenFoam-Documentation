# timeSelector 
## Class
Foam::timeSelector

## Description
A List of scalarRange for selecting times.

The timeSelector provides a convenient means of selecting multiple
times. A typical use would be the following:

```
timeSelector::addOptions();
// add other options
#include "setRootCase.H"
#include "createTime.H"
instantList timeDirs = timeSelector::select0(runTime, args);
...
forAll(timeDirs, timeI)
{
        ...
}
```

The result program would receive \b -time, @b -latestTime, @b -constant
and \b -noZero options. The @b -constant option explicitly includes the
\c constant/ directory in the time list and the \b -noZero option
explicitly excludes the \c 0/ directory from the time list.

There may however also be many cases in which neither the \c constant/
directory nor the \c 0/ directory contain particularly relevant
information. This might occur, for example, when post-processing
results. In this case, addOptions is called with optional boolean
arguments.

```
timeSelector::addOptions(false, true);
```

The first argument avoids adding the \b -constant option. The second
argument adds an additional \b -withZero option and also prevents the
\c 0/ directory from being included in the default time range and in the
\b -latestTime selection.

## SourceFiles
timeSelector.C

