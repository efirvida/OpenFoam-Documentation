# edgeFaceCirculator 
## Class
Foam::edgeFaceCirculator

## Description
Walks from starting face around edge.

Implicit description of edge:
- face
- index in face. edge is always between f[index] and f[index+1]
- direction (cell to walk into)

-# Use in-place: \n
        \code
            edgeFaceCirculator circ(..);
            // Optionally rotate to beginning: circ.setCanonical();

            // Walk
            do
            {
                Info<< "face:" << circ.face() << endl;
                ++circ;
            }
            while (circ != circ.end());
        \endcode

-# Use like STL iterator: \n
        \code
            edgeFaceCirculator circ(..);
            for
            (
                edgeFaceCirculator iter = circ.begin();
                iter != circ.end();
                ++iter
            )
            {
                Info<< "face:" << iter.face() << endl;
            }
        \endcode


## SourceFiles
edgeFaceCirculator.C

