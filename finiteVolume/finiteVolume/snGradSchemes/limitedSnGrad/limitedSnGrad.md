# limitedSnGrad 
## Class
Foam::fv::limitedSnGrad

## Description
Run-time selected snGrad scheme with limited non-orthogonal correction.

The limiter is controlled by a coefficient with a value between 0 and 1
which when 0 switches the correction off and the scheme behaves as
uncorrectedSnGrad, when set to 1 the full correction of the selected scheme
is used and when set to 0.5 the limiter is calculated such that the
non-orthogonal contribution does not exceed the orthogonal part.

Format:
        limited \<corrected scheme\> \<coefficient\>;

        or

        limited \<coefficient\>;  // Backward compatibility

## SourceFiles
limitedSnGrad.C

