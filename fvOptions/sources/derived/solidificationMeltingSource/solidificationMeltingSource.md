# solidificationMeltingSource 
## Class
Foam::fv::solidificationMeltingSource

## Description
This source is designed to model the effect of solidification and melting
processes, e.g. windhield defrosting.  The phase change occurs at the
melting temperature, \c Tmelt.

The presence of the solid phase in the flow field is incorporated into the
model as a momentum porosity contribution; the energy associated with the
phase change is added as an enthalpy contribution.

Based on the references:

      1. V.R. Voller and C. Prakash, A fixed grid numerical modelling
         methodology for convection-diffusion mushy phase-change problems,
         Int. J. Heat Mass Transfer 30(8):17091719, 1987.
      2. C.R. Swaminathan. and V.R. Voller, A general enthalpy model for
         modeling solidification processes, Metallurgical Transactions
         23B:651664, 1992.

The model generates a field \c \<name\>:alpha1 which can be visualised to
to show the melt distribution as a fraction [0-1]

## Usage
Example usage:
```
solidificationMeltingSource1
{
        type            solidificationMeltingSource;
        active          yes;

        solidificationMeltingSourceCoeffs
        {
            selectionMode   cellZone;
            cellZone        iceZone;

            Tmelt           273;
            L               334000;
            thermoMode      thermo;
            beta            50e-6;
            rhoRef          800;
        }
}
```

Where:

        Property     | Description             | Required    | Default value
        Tmelt        | Melting temperature [K] | yes         |
        L            | Latent heat of fusion [J/kg] | yes    |
        relax        | Relaxation coefficient [0-1] | no     | 0.9
        thermoMode   | Thermo mode [thermo|lookup] | yes     |
        rhoRef       | Reference (solid) density | yes       |
        rho          | Name of density field   | no          | rho
        T            | Name of temperature field | no        | T
        Cp           | Name of specific heat capacity field | no | Cp
        U            | Name of velocity field  | no          | U
        phi          | Name of flux field      | no          | phi
        Cu           | Model coefficient       | no          | 100000
        q            | Model coefficient       | no          | 0.001
        beta         | Thermal expansion coefficient [1/K] | yes |
        g            | Accelerartion due to gravity | no     |


## SourceFiles
solidificationMeltingSource.C
solidificationMeltingSourceIO.C

