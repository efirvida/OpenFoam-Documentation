# Circulator.T 
## Class
Foam::Circulator

## Description
Walks over a container as if it were circular. The container must have the
following members defined:
        - value_type
        - size_type
        - difference_type
        - iterator
        - reference

Examples

\code
        face f(identity(5));

        // Construct Circulator from the face
        Circulator<face> circ(f);

        // First check that the Circulator has a size to iterate over.
        // Then circulate around the list starting and finishing at the fulcrum.
        if (circ.size()) do
        {
            circ() += 1;

            Info<< "Iterate forwards over face : " << circ() << endl;

        } while (circ.circulate(CirculatorBase::CLOCKWISE));
\endcode

## SourceFiles
CirculatorI.H

