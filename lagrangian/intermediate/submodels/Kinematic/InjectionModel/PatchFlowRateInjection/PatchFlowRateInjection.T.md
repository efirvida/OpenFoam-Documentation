# PatchFlowRateInjection.T 
## Class
Foam::PatchFlowRateInjection

## Description
Patch injection, by using patch flow rate to determine concentration and
velocity.

User specifies:
      - Total mass to inject
      - Name of patch
      - Injection duration
      - Injection target concentration/carrier volume flow rate

Properties:
      - Initial parcel velocity given by local flow velocity
      - Parcel diameters obtained by distribution model
      - Parcels injected randomly across the patch

## SourceFiles
PatchFlowRateInjection.C

