# bladeModel 
## Class
Foam::bladeModel

## Description
Blade model class calculates:
        Linear interpolated blade twist and chord based on radial position
        Interpolation factor (for interpolating profile performance)

Input in list format:

        data
        (
            (profile1 (radius1 twist1 chord1))
            (profile1 (radius2 twist2 chord2))
        );

where:
        radius [m]
        twist [deg], converted to [rad] internally
        chord [m]

## SourceFiles
bladeModel.C

