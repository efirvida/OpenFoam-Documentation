# filmPyrolysisRadiativeCoupledMixedFvPatchScalarField 
## Class
Foam::filmPyrolysisRadiativeCoupledMixedFvPatchScalarField

## Description
Mixed boundary condition for temperature, to be used in the flow and
pyrolysis regions when a film region model is used.

Example usage:
```
myInterfacePatchName
{
        type            filmPyrolysisRadiativeCoupledMixed;
        Tnbr            T;
        kappa           fluidThermo;
        Qr              Qr;
        kappaName       none;
        filmDeltaDry    0.0;
        filmDeltaWet    3e-4;
        value           $internalField;
}
```

Needs to be on underlying mapped(Wall)FvPatch.
It calculates local field as:

```
        ratio = (filmDelta - filmDeltaDry)/(filmDeltaWet - filmDeltaDry)
```

when ratio = 1 is considered wet and the film temperature is fixed at
the wall. If ratio = 0 (dry) it emulates the normal radiative solid BC.

In between ratio 0 and 1 the gradient and value contributions are
weighted using the ratio field in the following way:

```
        qConv = ratio*htcwfilm*(Tfilm - *this);
        qRad = (1.0 - ratio)*Qr;
```

Then the solid can gain or loose energy through radiation or conduction
towards the film.

Notes:

- kappa and \c kappaName are inherited from temperatureCoupledBase.
- Qr is the radiative flux defined in the radiation model.


## See also
Foam::temperatureCoupledBase

## SourceFiles
filmPyrolysisRadiativeCoupledMixedFvPatchScalarField.C

