# codedFixedValuePointPatchField 
## Class
Foam::codedFixedValuePointPatchField

## Description
Constructs on-the-fly a new boundary condition (derived from
fixedValuePointPatchField) which is then used to evaluate.

Example:
```
movingWall
{
        type            codedFixedValue;
        value           uniform 0;
        name    rampedFixedValue;   // name of generated bc

        code
        #{
            operator==
            (
                vector(0,0,1)
                *min(10, 0.1*this->db().time().value())
            );
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

A special form is if the \c code section is not supplied. In this case
the code gets read from a (runTimeModifiable!) dictionary system/codeDict
which would have a corresponding entry

```
rampedFixedValue
{
        code
        #{
            operator==(min(10, 0.1*this->db().time().value()));
        #};
}
```

## See also
codedFixedValueFvPatchField

## SourceFiles
codedFixedValuePointPatchField.C

