# StandardWallInteraction.T 
## Class
Foam::StandardWallInteraction

## Description
Wall interaction model.

Three choices:
      - rebound - optionally specify elasticity and restitution coefficients
      - stick   - particles assigned zero velocity
      - escape  - remove particle from the domain

Example usage:
```
StandardWallInteractionCoeffs
{
        type        rebound; // stick, escape
        e           1;       // optional - elasticity coeff
        mu          0;       // optional - restitution coeff
}
```

