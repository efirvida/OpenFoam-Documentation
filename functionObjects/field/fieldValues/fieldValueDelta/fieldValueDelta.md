# fieldValueDelta 
## Class
Foam::functionObjects::fieldValues::fieldValueDelta

## Group
grpFieldFunctionObjects

## Description
This function object provides a differencing option between two 'field
value' function objects.

Example of function object specification:
```
fieldValueDelta1
{
        type            fieldValueDelta;
        libs ("libfieldFunctionObjects.so");
        operation       subtract;

        fieldValue1
        {
            ...
        }
        fieldValue2
        {
            ...
        }
}
```

## Usage

        Property     | Description             | Required    | Default value
        type         | type name: fieldValueDelta   | yes    |


The \c operation is one of:
\plaintable
       add           | add
       subtract      | subtract
       min           | minimum
       max           | maximum
       average       | average
\endplaintable

## See also
Foam::fieldValue

## SourceFiles
fieldValueDelta.C

