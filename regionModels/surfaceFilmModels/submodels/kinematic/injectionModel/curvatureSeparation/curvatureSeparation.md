# curvatureSeparation 
## Class
Foam::curvatureSeparation

## Description
Curvature film separation model

Assesses film curvature via the mesh geometry and calculates a force
balance of the form:

        F_sum = F_inertial + F_body + F_surface

If F_sum < 0, the film separates. Similarly, if F_sum > 0 the film will
remain attached.

Based on description given by
        Owen and D. J. Ryley. The flow of thin liquid films around corners.
        International Journal of Multiphase Flow, 11(1):51-62, 1985.


## SourceFiles
curvatureSeparation.C

