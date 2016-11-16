# symplectic 
## Class
Foam::sixDoFSolvers::symplectic

## Description
Symplectic 2nd-order explicit time-integrator for 6DoF solid-body motion.

Reference:
```
        Dullweber, A., Leimkuhler, B., & McLachlan, R. (1997).
        Symplectic splitting methods for rigid body molecular dynamics.
        The Journal of chemical physics, 107(15), 5840-5851.
```

Can only be used for explicit integration of the motion of the body,
i.e. may only be called once per time-step, no outer-correctors may be
applied.  For implicit integration with outer-correctors choose either
CrankNicolson or Newmark schemes.

Example specification in dynamicMeshDict:
```
solver
{
        type    symplectic;
}
```

## See also
Foam::sixDoFSolvers::CrankNicolson
Foam::sixDoFSolvers::Newmark

## SourceFiles
symplectic.C

