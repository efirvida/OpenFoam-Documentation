# rotorDiskSource 
## Class
Foam::fv::rotorDiskSource

## Description
Rotor disk source

Cell based momemtum source which approximates the mean effects of
rotor forces on a cylindrical region within the domain.

## Usage
Example usage:
```
rotorDiskSourceCoeffs
{
        fieldNames      (U);    // names of fields on which to apply source
        nBlades         3;      // number of blades
        tipEffect       0.96;   // normalised radius above which lift = 0

        inletFlowType   local;  // inlet flow type specification

        geometryMode    auto;   // geometry specification

        refDirection    (-1 0 0); // reference direction
                                  // - used as reference for psi angle

        trimModel       fixed;  // fixed || targetForce

        flapCoeffs
        {
            beta0           0;  // coning angle [deg]
            beta1c          0;  // lateral flapping coeff (cos coeff)
            beta2s          0;  // longitudinal flapping coeff (sin coeff)
        }

        blade
        {
            // see bladeModel.H for documentation
        }

        profiles
        {
            profile1
            {
                type    lookup; // lookup || series
                ...
                // see lookupProfile.H or seriesProfile.H for documentation
            }
            profile2
            {
                ...
            }
        }
}
```

Where:
Valid options for the \c geometryMode entry include:
    - auto          : determine rototor co-ord system from cells
    - specified     : specified co-ord system

Valid options for the \c inletFlowType entry include:
    - fixed         : specified velocity
    - local         : use local flow conditions
- surfaceNormal : specified normal velocity (positive towards rotor)

## See also
Foam::bladeModel
Foam::lookupProfile
Foam::seriesProfile

## SourceFiles
rotorDiskSource.C
rotorDiskSourceTemplates.C

