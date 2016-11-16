# atmBoundaryLayer 
## Class
Foam::atmBoundaryLayer

## Group
grpRASBoundaryConditions grpInletBoundaryConditions

## Description
This class provides functions to evaluate the velocity and turbulence
distributions appropriate for atmospheric boundary layers (ABL).

The profile is derived from the friction velocity, flow direction and
"vertical" direction:

        \f[
            U = \frac{U^*}{\kappa} ln\left(\frac{z - z_g + z_0}{z_0}\right)
        \f]

        \f[
            k = \frac{(U^*)^2}{\sqrt{C_mu}}
        \f]

        \f[
            \epsilon = \frac{(U^*)^3}{\kappa(z - z_g + z_0)}
        \f]

where
\vartable
        U^*     | Friction velocity
        \kappa  | von Karman's constant
        C_mu    | Turbulence viscosity coefficient
        z       | Vertical coordinate
        z_0     | Surface roughness height [m]
        z_g     | Minimum z-coordinate [m]
\endvartable
and
        \f[
            U^* = \kappa\frac{U_{ref}}{ln\left(\frac{Z_{ref} + z_0}{z_0}\right)}
        \f]
where
\vartable
        U_{ref} | Reference velocity at \f$Z_{ref}\f$ [m/s]
        Z_{ref} | Reference height [m]
\endvartable

Use in the atmBoundaryLayerInletVelocity, atmBoundaryLayerInletK and
atmBoundaryLayerInletEpsilon boundary conditions.

Reference:
        D.M. Hargreaves and N.G. Wright,  "On the use of the k-epsilon model
        in commercial CFD software to model the neutral atmospheric boundary
        layer", Journal of Wind Engineering and Industrial Aerodynamics
        95(2007), pp 355-369.

## Usage

        Property     | Description                      | Required  | Default
        flowDir      | Flow direction                   | yes       |
        zDir         | Vertical direction               | yes       |
        kappa        | von Karman's constant            | no        | 0.41
        Cmu          | Turbulence viscosity coefficient | no        | 0.09
        Uref         | Reference velocity [m/s]         | yes       |
        Zref         | Reference height [m]             | yes       |
        z0           | Surface roughness height [m]     | yes       |
        zGround      | Minimum z-coordinate [m]         | yes       |


Example of the boundary condition specification:
```
ground
{
        type            atmBoundaryLayerInletVelocity;
        flowDir         (1 0 0);
        zDir            (0 0 1);
        Uref            10.0;
        Zref            20.0;
        z0              uniform 0.1;
        zGround         uniform 0.0;
}
```

## Note
D.M. Hargreaves and N.G. Wright recommend Gamma epsilon in the
k-epsilon model should be changed from 1.3 to 1.11 for consistency.
The roughness height (Er) is given by Er = 20 z0 following the same
reference.

## SourceFiles
atmBoundaryLayer.C

