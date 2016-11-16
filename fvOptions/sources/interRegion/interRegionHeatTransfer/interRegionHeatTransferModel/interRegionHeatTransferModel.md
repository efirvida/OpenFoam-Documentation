# interRegionHeatTransferModel 
## Class
Foam::fv::interRegionHeatTransferModel

## Description
Base class for inter region heat exchange. The derived classes must
provide the heat transfer coeffisine (htc) which is used as follows
in the energy equation.

     \f[
        -htc*Tmapped + Sp(htc, T)
     \f]

