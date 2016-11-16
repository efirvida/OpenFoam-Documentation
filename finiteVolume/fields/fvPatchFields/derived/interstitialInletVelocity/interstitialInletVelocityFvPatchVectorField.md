# interstitialInletVelocityFvPatchVectorField 
## Class
Foam::interstitialInletVelocityFvPatchVectorField

## Description
Inlet velocity in which the actual interstitial velocity is calculated
by dividing the specified inletVelocity field with the local phase-fraction.

Example of the boundary condition specification:
```
inlet
{
        type              interstitialInletVelocity;
        inletVelocity     uniform (0 0.2 0);// Non-interstitial inlet velocity
        alpha             alpha.particles;  // Name of the phase-fraction field
        value             uniform (0 0 0);
}
```

## SourceFiles
interstitialInletVelocityFvPatchVectorField.C

