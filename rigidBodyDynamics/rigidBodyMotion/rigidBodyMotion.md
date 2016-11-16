# rigidBodyMotion 
## Class
Foam::RBD::rigidBodyMotion

## Description
Six degree of freedom motion for a rigid body.

Angular momentum stored in body fixed reference frame.  Reference
orientation of the body (where Q = I) must align with the cartesian axes
such that the Inertia tensor is in principle component form.  Can add
restraints (e.g. a spring) and constraints (e.g. motion may only be on a
plane).

The time-integrator for the motion is run-time selectable with options for
symplectic (explicit), Crank-Nicolson and Newmark schemes.

## SourceFiles
rigidBodyMotionI.H
rigidBodyMotion.C
rigidBodyMotionIO.C

