# FieldActivatedInjection.T 
## Class
Foam::FieldActivatedInjection

## Description
Injection at specified positions, with the conditions:

For injection to be allowed
```
      factor*referenceField[celli] >= thresholdField[celli]
```
      where:
        - \c referenceField is the field used to supply the look-up values
        - \c thresholdField supplies the values beyond which the injection is
            permitted.

Limited to a user-supplied number of injections per injector location

## SourceFiles
FieldActivatedInjection.C

