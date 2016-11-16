# codedMixedFvPatchField 
## Class
Foam::codedMixedFvPatchField

## Group
grpGenericBoundaryConditions

## Description
Constructs on-the-fly a new boundary condition (derived from
mixedFvPatchField) which is then used to evaluate.

## Usage
Example:
```
<patchName>
{
        type            codedMixed;

        refValue        uniform (0 0 0);
        refGradient     uniform (0 0 0);
        valueFraction   uniform 1;

        name    rampedMixed;   // name of generated BC

        code
        #{
            this->refValue() =
                vector(1, 0, 0)
               *min(10, 0.1*this->db().time().value());
            this->refGrad() = Zero;
            this->valueFraction() = 1.0;
        #};

        //codeInclude
        //#{
        //    #include "fvCFD.H"
        //#};

        //codeOptions
        //#{
        //    -I$(LIB_SRC)/finiteVolume/lnInclude
        //#};
}
```

A special form is if the 'code' section is not supplied. In this case
the code gets read from a (runTimeModifiable!) dictionary system/codeDict
which would have a corresponding entry

```
<patchName>
{
        code
        #{
            this->refValue() = min(10, 0.1*this->db().time().value());
            this->refGrad() = Zero;
            this->valueFraction() = 1.0;
        #};
}
```

## See also
Foam::dynamicCode
Foam::functionEntries::codeStream

## SourceFiles
codedMixedFvPatchField.C

