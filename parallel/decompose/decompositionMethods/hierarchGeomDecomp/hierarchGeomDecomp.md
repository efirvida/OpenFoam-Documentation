# hierarchGeomDecomp 
## Class
Foam::hierarchGeomDecomp

## Description
Does hierarchical decomposition of points. Works by first sorting the
points in x direction into equal sized bins, then in y direction and
finally in z direction.

Uses single array to hold decomposition which is indexed as if it is a
3 dimensional array:

        finalDecomp[i,j,k] is indexed as

        i*n[0]*n[1] + j*n[1] + k

E.g. if we're sorting 'xyz': the first sort (over the x-component)
determines in which x-domain the point goes. Then for each of the x-domains
the points are sorted in y direction and each individual x-domain gets
split into three y-domains. And similar for the z-direction.

Since the domains are of equal size the maximum difference in size is
n[0]*n[1] (or n[1]*n[2]?) (small anyway)


## SourceFiles
hierarchGeomDecomp.C

