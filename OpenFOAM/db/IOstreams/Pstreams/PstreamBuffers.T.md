# PstreamBuffers.T 
## Class
Foam::PstreamBuffers

## Description
Buffers for inter-processor communications streams (UOPstream, UIPstream).

Use UOPstream to stream data into buffers, call finishedSends() to
notify that data is in buffers and then use IUPstream to get data out
of received buffers. Works with both blocking and nonBlocking. Does
not make much sense with scheduled since there you would not need these
explicit buffers.

Example usage:

        PstreamBuffers pBuffers(Pstream::nonBlocking);

        for (label proci = 0; proci < Pstream::nProcs(); proci++)
        {
            if (proci != Pstream::myProcNo())
            {
                someObject vals;

                UOPstream str(proci, pBuffers);
                str << vals;
            }
        }

        pBuffers.finishedSends();   // no-op for blocking

        for (label proci = 0; proci < Pstream::nProcs(); proci++)
        {
            if (proci != Pstream::myProcNo())
            {
                UIPstream str(proci, pBuffers);
                someObject vals(str);
            }
        }


## SourceFiles
PstreamBuffers.C

