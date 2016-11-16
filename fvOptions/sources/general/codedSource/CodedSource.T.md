# CodedSource.T 
## Class
Foam::fv::codedSource

## Description
   Constructs on-the-fly fvOption source

The hook functions take the following arguments:

codeCorrect
(
        GeometricField<Type, fvPatchField, volMesh>& field
)

codeAddSup
(
        fvMatrix<Type}>& eqn,
        const label fieldi
)

constrain
(
        fvMatrix<Type}>& eqn,
        const label fieldi
)

where :
        field is the field in fieldNames
        eqn is the fvMatrix

## Usage
Example usage in controlDict:
```
energySource
{
        type            scalarCodedSource;

        active          yes;

        scalarCodedSourceCoeffs
        {
            selectionMode   all;

            fieldNames      (h);
            name    sourceTime;

            codeInclude
            #{

            #};

            codeCorrect
            #{
                Pout<< "**codeCorrect**" << endl;
            #};

            codeAddSup
            #{
                const Time& time = mesh().time();
                const scalarField& V = mesh_.V();
                scalarField& heSource = eqn.source();
                heSource -= 0.1*sqr(time.value())*V;
            #};

            codeSetValue
            #{
                Pout<< "**codeSetValue**" << endl;
            #};

            // Dummy entry. Make dependent on above to trigger recompilation
            code
            #{
                $codeInclude
                $codeCorrect
                $codeAddSup
                $codeSetValue
            #};
        }

        sourceTimeCoeffs
        {
            // Dummy entry
        }
}
```


## SourceFiles
codedSource.C

