# pressure 
## Class
Foam::functionObjects::pressure

## Group
grpFieldFunctionObjects

## Description
This function object includes tools to manipulate the pressure into
different forms.  These currently include:

- static pressure
        \f[
            p = \rho p_k
        \f]
- total pressure
        \f[
            p_0 = p_{ref} + p + 0.5 \rho |U|^2
        \f]
- static pressure coefficient
        \f[
            Cp = \frac{p - p_{\inf}}{0.5 \rho_{\inf} |U_{\inf}|^2}
        \f]
- total pressure coefficient
        \f[
            Cp_0 = \frac{p_0 - p_{\inf}}{0.5 \rho_{\inf} |U_{\inf}|^2}
        \f]

where
\vartable
        \rho        | Density [kg/m3]
        U           | Velocity [m/s]
        \rho_{\inf} | Freestream density [kg/m3]
        p_{\inf}    | Freestream pressure [Pa]
        U_{\inf}    | Freestream velocity [m/s]
        p_k         | Kinematic pressure (p/rho)[m2/s2]
        p           | Pressure [Pa]
        p_0         | Total pressure [Pa]
        p_{ref}     | Reference pressure level [Pa]
        Cp          | Pressure coefficient
        Cp_0        | Total pressure coefficient
\endvartable

The function object will operate on both kinematic (\f$ p_k \f$) and static
pressure (\f$ p \f$) fields, and the result is written as a
volScalarField.

The modes of operation are:

        Mode                        | calcTotal | calcCoeff
        Static pressure             | no        | no
        Total pressure              | yes       | no
        Pressure coefficient        | no        | yes
        Total pressure coefficient  | yes       | yes


Example of function object specification to calculate pressure coefficient:
```
pressure1
{
        type        pressure;
        libs ("libfieldFunctionObjects.so");
        ...
        calcTotal   no;
        calcCoeff   yes;
}
```

## Usage

        Property     | Description                 | Required   | Default value
        type         | type name: pressure    | yes        |
        field        | Name of the pressure field  | no         | p
        U            | Name of the velocity field  | no         | U
        rho          | Name of the density field   | no         | rho
        result       | Name of the resulting field | no         | derived from p
        calcTotal    | Calculate total coefficient | yes        |
        pRef         | Reference pressure for total pressure | no | 0
        calcCoeff    | Calculate pressure coefficient | yes  |
        pInf         | Freestream pressure for coefficient calculation | no |
        UInf         | Freestream velocity for coefficient calculation | no |
        rhoInf       | Freestream density for coefficient calculation  | no |


## See also
Foam::functionObjects::fieldExpression
Foam::functionObjects::fvMeshFunctionObject

## SourceFiles
pressure.C

