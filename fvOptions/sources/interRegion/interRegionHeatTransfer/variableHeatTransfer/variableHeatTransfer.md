# variableHeatTransfer 
## Class
Foam::fv::variableHeatTransfer

## Description
Variable heat transfer model depending on local values. The area of contact
between regions (area) must be provided. The Nu number is calculated as:

        Nu = a*pow(Re, b)*pow(Pr, c)

and the heat transfer coefficient as:

        htc = Nu*K/ds

where:
        K is the heat conduction
        ds is the strut diameter

