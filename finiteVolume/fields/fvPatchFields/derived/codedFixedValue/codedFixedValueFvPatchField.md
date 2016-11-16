# codedFixedValueFvPatchField 
## Class
Foam::codedFixedValueFvPatchField

## Group
grpGenericBoundaryConditions

## Description
Constructs on-the-fly a new boundary condition (derived from
fixedValueFvPatchField) which is then used to evaluate.

## Usage
Example:
```
<patchName>
{
        type            codedFixedValue;
        value           uniform 0;
        name    rampedFixedValue;   // name of generated BC

        code
        #{
            operator==(min(10, 0.1*this->db().time().value()));
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
the code is read from a (runTimeModifiable!) dictionary system/codeDict
which would have a corresponding entry:

```
<patchName>
{
        code
        #{
            operator==(min(10, 0.1*this->db().time().value()));
        #};
}
```

## See also
Foam::dynamicCode
Foam::functionEntries::codeStream

## SourceFiles
codedFixedValueFvPatchField.C

