# SLGThermo 
## Class
Foam::SLGThermo

## Description
Thermo package for (S)olids (L)iquids and (G)ases
Takes reference to thermo package, and provides:
- carrier : components of thermo - access to elemental properties
- liquids : liquid components - access  to elemental properties
- solids  : solid components - access  to elemental properties

If thermo is not a multi-component thermo package, carrier is NULL.
Similarly, if no liquids or solids are specified, their respective
pointers will also be NULL.

Registered to the mesh so that it can be looked-up

## SourceFiles
SLGThermo.C

