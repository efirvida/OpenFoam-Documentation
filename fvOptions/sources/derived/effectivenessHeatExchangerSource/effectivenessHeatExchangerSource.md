# effectivenessHeatExchangerSource 
## Class
Foam::fv::effectivenessHeatExchangerSource

## Description
Heat exchanger source model, in which the heat exchanger is defined as a
selection of cells.

The total heat exchange source is given by:
\f[
        Q_t = e(\phi, \dot{m}_2) (T_2 - T_1) \phi c_p
\f]

where:
\vartable
        Q_t       | total heat source
        e(\phi,\dot{m}_2) | effectivenes table
        \phi      | net mass flux entering heat exchanger [kg/s]
        \dot{m}_2 | secondary mass flow rate [kg/s]
        T_1       | primary inlet temperature [K]
        T_2       | secondary inlet temperature [K]
        c_p       | specific heat capacity [J/kg/K]
\endvartable


The distribution inside the hear exchanger is given by:
\f[
        Q_c = \frac{V_c |U_c| (T_c - T_{ref})}{\sum(V_c |U_c| (T_c - T_{ref}))}
\f]

where:
\vartable
        Q_c     | source for cell
        V_c     | volume of the cell [m3]
        U_c     | local cell velocity [m/s]
        T_c     | local call temperature [K]
        T_{ref} | min or max(T) in cell zone depending on the sign of Q_t [K]
\endvartable

## Usage
Example usage:
```
effectivenessHeatExchangerSource1
{
        type            effectivenessHeatExchangerSource;
        active          yes;

        effectivenessHeatExchangerSourceCoeffs
        {
            selectionMode   cellZone;
            cellZone        porosity;

            secondaryMassFlowRate   1.0;
            secondaryInletT         336;
            primaryInletT           293;
            faceZone                facesZoneInletOriented;
            outOfBounds             clamp;
            fileName                "effTable";
        }
}
```

The effectiveness table is described in terms of the primary and secondary
mass flow rates.  For example, the table:

                           secondary MFR
                       |  0.1   0.2   0.3
                  -----+-----------------
                  0.02 |   A     B     C
     primary MFR  0.04 |   D     E     F
                  0.06 |   G     H     I


Is specified by the following:

        (
            0.02
            (
                (0.1    A)
                (0.2    B)
                (0.3    C)
            ),
            0.04
            (
                (0.1    D)
                (0.2    E)
                (0.3    F)
            ),
            0.06
            (
                (0.1    G)
                (0.2    H)
                (0.3    I)
            )
        );


## Note
## - the table with name "fileName" should have the same units as the
  secondary mass flow rate and kg/s for phi
## - faceZone is the faces at the inlet of the cellzone, it needs to be
  created with flip map flags. It is used to integrate the net mass flow
  rate into the heat exchanger


## SourceFiles
effectivenessHeatExchangerSource.C

