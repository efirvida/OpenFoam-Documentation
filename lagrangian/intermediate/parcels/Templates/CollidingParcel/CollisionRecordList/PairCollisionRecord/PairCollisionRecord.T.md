# PairCollisionRecord.T 
## Class
Foam::PairCollisionRecord

## Description

Record of a collision between the particle holding the record and
the particle with the stored id.

The access status of the record is to be coded in the
origProcOfOther data member.  The actual processor is offset by
+1.  A negative value means that the record has not been accessed,
positive means that it has.

## SourceFiles
PairCollisionRecordI.H
PairCollisionRecord.C
PairCollisionRecordIO.C

