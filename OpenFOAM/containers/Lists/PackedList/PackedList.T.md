# PackedList.T 
## Class
Foam::PackedList

## Description
A dynamically allocatable list of packed unsigned integers.

The list resizing is similar to DynamicList, thus the methods clear()
and setSize() behave like their DynamicList counterparts and the methods
reserve() and setCapacity() can be used to influence the allocation.

The number of bits per item is specified by the template parameter nBits.

## Note
In a const context, the '[]' operator simply returns the stored value,
with out-of-range elements returned as zero.
In a non-const context, the '[]' operator returns an iteratorBase, which
might not have a valid reference for out-of-range elements.
The iteratorBase class handles the assignment of new values.

Using the iteratorBase as a proxy allows assignment of values
between list elements. Thus the following bit of code works as expected:
\code
        list[1] = list[5];      // value assignment, not iterator position
        list[2] = list[5] = 4;  // propagates value
        list[1] = list[5] = list[6];  // propagates value
\endcode

Using get() or the '[]' operator are similarly fast. Looping and reading
via an iterator is approx. 15% slower, but can be more flexible.

Using the set() operator (and the '[]' operator) are marginally slower
(approx. 5%) than using an iterator, but the set() method has the
advantage of also returning a bool if the value changed.  This can be
useful for branching on changed values.

\code
        list[5] = 4;
        changed = list.set(5, 8);
        if (changed) ...
\endcode

The lazy evaluation used means that reading an out-of-range element
returns zero, but does not affect the list size.  Even in a non-const
context, only the assigment itself causes the element to be created.
For example,
\code
        list.resize(4);
        Info<< list[10] << "\n";  // print zero, but doesn't adjust list
        list[8] = 1;
\endcode

Also note that all unused internal storage elements are guaranteed to
always be bit-wise zero. This property must not be violated by any
inheriting classes.

In addition to the normal output format, PackedList also supports a
compact ASCII format that may be convenient for user input in some
situations. The general format is a group of index/value pairs:
```
        { (index1 value1) (index2 value2) (index3 value3) }
```
The bool specialization just uses the indices corresponding to
non-zero entries instead of a index/value pair:
```
        { index1 index2 index3 }
```
In both cases, the supplied indices can be randomly ordered.

## See also
Foam::DynamicList

## SourceFiles
PackedListI.H
PackedList.C

