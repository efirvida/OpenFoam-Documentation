# ConeNozzleInjection.T 
## Class
Foam::ConeNozzleInjection

## Description
Cone injection.

User specifies:
      - time of start of injection
      - injector position
      - direction (along injection axis)
      - parcel flow rate
      - inner and outer half-cone angles

Properties:
      - Parcel diameters obtained by size distribution model.

      - Parcel velocity is calculated as:
        - Constant velocity:
```
          U = \<specified by user\>
```

        - Pressure driven velocity:
```
          U = sqrt(2*(Pinj - Pamb)/rho)
```

        - Flow rate and discharge:
```
          U = V_dot/(A*Cd)
```

## SourceFiles
ConeNozzleInjection.C

