# Implicit.T 
## Class
Foam::PackingModels::Implicit

## Description
Implicit model for applying an inter-particle stress to the particles.

The time evolution of particulate volume fraction is solved for implicitly
on the eulerian mesh. The computed flux is then applied to the lagrangian
field. The gravity force can optionally be applied to the particles as part
of this model, using the keyword "applyGravity".

## SourceFiles
Implicit.C

