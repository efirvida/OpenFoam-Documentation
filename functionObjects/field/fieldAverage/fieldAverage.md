# fieldAverage 
## Class
Foam::functionObjects::fieldAverage

## Group
grpFieldFunctionObjects

## Description
This function object calculates average quantities for a user-specified
selection of volumetric and surface fields.  Fields are entered as a list
of sub-dictionaries, which indicate the type of averages to perform, and
can be updated during the calculation.  The current options include:
- \c mean: arithmetic mean:
        \f[
            \overline{x} = \frac{1}{N}\displaystyle\sum\limits_{i=0}^N x_i
        \f]
- \c prime2Mean: prime-squared mean
        \f[
            \overline{x'}^2 = \frac{1}{N}\displaystyle\sum\limits_{i=0}^N
            (x_i - \overline{x})^2
        \f]
- base: average over 'time', or 'iteration' (\f$N\f$ in the above)
- window: optional averaging window, specified in 'base' units

Average field names are constructed by concatenating the base field with
the averaging type, e.g. when averaging field 'U', the resultant fields
are:
- arithmetic mean field, UMean
- prime-squared field, UPrime2Mean

Information regarding the number of averaging steps, and total averaging
time are written on a per-field basis to the
\c "<functionObject name>Properties" dictionary, located in \<time\>/uniform

When restarting form a previous calculation, the averaging is continuous or
may be restarted using the \c restartOnRestart option.

The averaging process may be restarted after each calculation output time
using the \c restartOnOutput option or restarted periodically using the \c
periodicRestart option and setting \c restartPeriod to the required
averaging period.

Example of function object specification:
```
fieldAverage1
{
        type fieldAverage;
        libs ("libfieldFunctionObjects.so");
        ...
        restartOnRestart    false;
        restartOnOutput     false;
        periodicRestart     false;
        restartPeriod       0.002;
        fields
        (
            U
            {
                mean            on;
                prime2Mean      on;
                base            time;
                window          10.0;
                windowName      w1;
            }
            p
            {
                mean            on;
                prime2Mean      on;
                base            time;
            }
        );
}
```

## Usage

        Property        | Description           | Required    | Default value
        type            | type name: fieldAverage | yes |
        restartOnRestart  | Restart the averaging on restart | no | no
        restartOnOutput   | Restart the averaging on output | no | no
        periodicRestart | Periodically restart the averaging | no | no
        restartPeriod   | Periodic restart period | conditional |
        fields          | list of fields and averaging options | yes |



## Note
To employ the \c prime2Mean option, the \c mean option must be selecetd.

## See also
Foam::functionObjects::fvMeshFunctionObject
Foam::functionObject

## SourceFiles
fieldAverage.C
fieldAverageTemplates.C
fieldAverageItem.C

