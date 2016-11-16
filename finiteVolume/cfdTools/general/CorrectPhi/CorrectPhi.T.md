# CorrectPhi.T 
## Class
Foam::CorrectPhi

## Description
Flux correction functions to ensure continuity.

Required during start-up, restart, mesh-motion etc. when non-conservative
fluxes may adversely affect the prediction-part of the solution algorithm
(the part before the first pressure solution which would ensure continuity).
This is particularly important for VoF and other multi-phase solver in
which non-conservative fluxes cause unboundedness of the phase-fraction.

## SourceFiles
CorrectPhi.C

