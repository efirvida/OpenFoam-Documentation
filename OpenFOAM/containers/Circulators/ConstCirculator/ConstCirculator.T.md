# ConstCirculator.T 
## Class
Foam::ConstCirculator

## Description
Walks over a container as if it were circular. The container must have the
following members defined:
        - value_type
        - size_type
        - difference_type
        - const_iterator
        - const_reference

Examples:

\code
        face f(identity(5));

        // Construct circulator from the face
        ConstCirculator<face> circ(f);

        // First check that the circulator has a size to iterate over.
        // Then circulate around the list starting and finishing at the fulcrum.
        if (circ.size()) do
        {
            Info<< "Iterate forwards over face : " << circ() << endl;

        } while (circ.circulate(CirculatorBase::CLOCKWISE));
\endcode

\code
        face f(identity(5));

        ConstCirculator<face> circClockwise(f);
        ConstCirculator<face> circAnticlockwise(f);

        if (circClockwise.size() && circAnticlockwise.size()) do
        {
            Info<< "Iterate forward over face :" << circClockwise() << endl;
            Info<< "Iterate backward over face:" << circAnticlockwise() << endl;
        }
        while
        (
            circClockwise.circulate(CirculatorBase::CLOCKWISE),
            circAnticlockwise.circulate(CirculatorBase::ANTICLOCKWISE)
        );
\endcode

## SourceFiles
ConstCirculatorI.H

