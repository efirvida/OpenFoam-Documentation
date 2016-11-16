# Sine.T 
## Class
Foam::Function1Types::Sine

## Description
Templated sine function with support for an offset level.

        \f[
            a sin(2 \pi f (t - t_0)) s + l
        \f]

where

\vartable
        symbol  | Description       | Data type
        a       | Amplitude         | Function1<scalar>
        f       | Frequency [1/s]   | Function1<scalar>
        s       | Type scale factor | Function1<Type>
        l       | Type offset level | Function1<Type>
        t_0     | Start time [s]    | scalar
        t       | Time [s]          | scalar
\endvartable

Example for a scalar:
```
        <entryName> sine;
        <entryName>Coeffs
        {
            frequency 10;
            amplitude 0.1;
            scale     2e-6;
            level     2e-6;
        }
```

Example for a vector:
```
        <entryName> sine;
        <entryName>Coeffs
        {
            frequency 10;
            amplitude 1;
            scale     (1 0.1 0);
            level     (10 1 0);
        }
```

## SourceFiles
Sine.C

