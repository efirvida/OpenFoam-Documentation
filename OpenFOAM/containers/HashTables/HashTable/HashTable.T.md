# HashTable.T 
## Class
Foam::HashTable

## Description
An STL-conforming hash table.

## Note
Hashing index collisions are handled via chaining using a singly-linked
list with the colliding entry being added to the head of the linked
list. Thus copying the hash table (or indeed even resizing it) will
often result in a different hash order. Use a sorted table-of-contents
when the hash order is important.

## SourceFiles
HashTableI.H
HashTable.C
HashTableIO.C

