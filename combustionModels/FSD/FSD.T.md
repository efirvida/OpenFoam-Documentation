# FSD.T 
## Class
Foam::combustionModels::FSD

## Description

Flame Surface Dennsity (FDS) combustion model.

The fuel source term is given by mgft*pc*omegaFuelBar.

where:
          mgft: filtered flame area.
          pc:   probability of the combustion progress.
          omegaFuelBar: filtered consumption speed per unit of flame area.

pc is considered from the IFC solution.
omegaFuelBar is calculated solving a relaxation equation which tends to
omegaEq. This omegaEq is obtained from the flamelet solution for
different strain rates and fit using a expential distribution.

The spacial distribution of the consumption speed (omega) is obtained also
from a strained flamelet solution and it is assumed to have a guassian
distribution.

If the grid resolution is not enough to resolve the flame, the consumption
speed distribution is linearly thickened conserving the overall heat
release.

If the turbulent fluctuation of the mixture fraction at the sub-grid level
is large (>1e-04) then a beta pdf is used for filtering.

At the moment the flame area combustion model is only fit to work in a LES
frame work. In RAS the subgrid fluctuation has to be solved by an extra
transport equation.

## SourceFiles
FSD.C

