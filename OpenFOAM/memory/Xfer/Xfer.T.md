# Xfer.T 
## Class
Foam::Xfer

## Description
A simple container for copying or transferring objects of type \<T\>.

The wrapped object of type \<T\> must implement a transfer() method and
an operator=() copy method.

Since it is decided upon construction of the Xfer object whether the
parameter is to be copied or transferred, the contents of the resulting
Xfer object can be transferred unconditionally. This greatly simplifies
defining constructors or methods in other classes with mixed
transfer/copy semantics without requiring 2^N different versions.

When transferring between dissimilar types, the xferCopyTo() and
xferMoveTo() functions can prove useful. An example is transferring
from a DynamicList to a List.  Since the
List\<T\>::transfer(List\<T\>&) method could result in some allocated
memory becoming inaccessible, the xferMoveTo() function should be used to
invoke the correct List\<T\>::transfer(DynamicList\<T\>&) method.

\code
        DynamicList<label> dynLst;
        ...
        labelList plainLst( xferMoveTo<labelList>(dynLst) );
\endcode

Of course, since this example is a very common operation, the
DynamicList::xfer() method transfers to a plain List anyhow.
It would thus be simpler (and clearer) just to use the following code:

\code
        DynamicList<label> dynLst;
        ...
        labelList plainLst(dynLst.xfer());
\endcode

## See also
xferCopy, xferCopyTo, xferMove, xferMoveTo, xferTmp

## SourceFiles
XferI.H

