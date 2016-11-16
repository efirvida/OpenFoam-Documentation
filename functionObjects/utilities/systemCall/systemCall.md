# systemCall 
## Class
Foam::functionObjects::systemCall

## Group
grpUtilitiesFunctionObjects

## Description
This function object executes system calls, entered in the form of a
string lists.  Calls can be made at the following points in the
calculation:
- every time step
- every output time
- end of the calculation

Example of function object specification:
```
systemCall1
{
        type        systemCall;
        libs        ("libutilityFunctionObjects.so");
        ...
        executeCalls
        (
            "echo execute"
        );
        writeCalls
        (
            "echo \*\*\* writing data \*\*\*"
        );
        endCalls
        (
            "echo \*\*\* writing .bashrc \*\*\*"
            "cat ~/.bashrc"
            "echo \*\*\* done \*\*\*"
        );
}
```

## Usage

        Property     | Description             | Required    | Default value
        type         | type name: systemCall   | yes         |
        executeCalls | list of calls on execute | yes        |
        writeCalls   | list of calls on write  | yes         |
        endCalls     | list of calls on end    | yes         |


## Note
Since this function object executes system calls, there is a potential
security risk.  In order to use the \c systemCall function object, the
\c allowSystemOperations must be set to '1'; otherwise, system calls will
not be allowed.

## See also
Foam::functionObject
Foam::functionObjects::timeControl

## SourceFiles
systemCall.C

