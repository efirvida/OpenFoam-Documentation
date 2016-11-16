# Square.T 
## Class
Foam::Function1Types::Square

## Description
Templated square-wave function with support for an offset level.

        \f[
            a square(f (t - t_0)) s + l
        \f]

where

\f$ square(t) \f$ is the square-wave function in range \f$ [-1, 1] \f$
with a mark/space ratio of \f$ r \f$

\vartable
        symbol  | Description       | Data type         | Default
        a       | Amplitude         | Function1<scalar> |
        f       | Frequency [1/s]   | Function1<scalar> |
        s       | Type scale factor | Function1<Type>   |
        l       | Type offset level | Function1<Type>   |
        t_0     | Start time [s]    | scalar            | 0
        r       | mark/space ratio  | scalar            | 1
        t       | Time [s]          | scalar
\endvartable

Example for a scalar:
```
        <entryName> square;
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
        <entryName> square;
        <entryName>Coeffs
        {
            frequency 10;
            amplitude 1;
            scale     (1 0.1 0);
            level     (10 1 0);
        }
```

## SourceFiles
Square.C

