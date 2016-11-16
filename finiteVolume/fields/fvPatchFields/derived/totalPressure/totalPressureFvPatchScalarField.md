# totalPressureFvPatchScalarField 
## Class
Foam::totalPressureFvPatchScalarField

## Group
grpInletBoundaryConditions grpOutletBoundaryConditions

## Description
This boundary condition provides a total pressure condition.  Four
variants are possible:

1. incompressible subsonic:
        \f[
            p_p = p_0 - 0.5 |U|^2
        \f]
        where
        \vartable
            p_p     | incompressible pressure at patch [m2/s2]
            p_0     | incompressible total pressure [m2/s2]
            U       | velocity
        \endvartable

2. compressible subsonic:
        \f[
            p_p = p_0 - 0.5 \rho |U|^2
        \f]
        where
        \vartable
            p_p     | pressure at patch [Pa]
            p_0     | total pressure [Pa]
            \rho    | density [kg/m3]
            U       | velocity
        \endvartable

3. compressible transonic (\f$\gamma = 1\f$):
        \f[
            p_p = \frac{p_0}{1 + 0.5 \psi |U|^2}
        \f]
        where
        \vartable
            p_p     | pressure at patch [Pa]
            p_0     | total pressure [Pa]
            G       | coefficient given by \f$\frac{\gamma}{1-\gamma}\f$
        \endvartable

4. compressible supersonic (\f$\gamma > 1\f$):
        \f[
            p_p = \frac{p_0}{(1 + 0.5 \psi G |U|^2)^{\frac{1}{G}}}
        \f]
        where
        \vartable
            p_p     | pressure at patch [Pa]
            p_0     | total pressure [Pa]
            \gamma  | ratio of specific heats (Cp/Cv)
            \psi    | compressibility [m2/s2]
            G       | coefficient given by \f$\frac{\gamma}{1-\gamma}\f$
        \endvartable

The modes of operation are set by the dimensions of the pressure field
to which this boundary condition is applied, the \c psi entry and the value
of \c gamma:

        Mode                    | dimensions | psi   | gamma
        incompressible subsonic | p/rho      |       |
        compressible subsonic   | p          | none  |
        compressible transonic  | p          | psi   | 1
        compressible supersonic | p          | psi   | > 1



## Usage

        Property     | Description                | Required | Default value
        U            | Velocity field name        | no       | U
        phi          | Flux field name            | no       | phi
        rho          | Density field name         | no       | rho
        psi          | Compressibility field name | no       | none
        gamma        | (Cp/Cv)                    | no       | 1
        p0           | Total pressure             | yes      |


Example of the boundary condition specification:
```
<patchName>
{
        type            totalPressure;
        p0              uniform 1e5;
}
```

## See also
Foam::fixedValueFvPatchField

## SourceFiles
totalPressureFvPatchScalarField.C

