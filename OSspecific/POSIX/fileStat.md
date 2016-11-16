# fileStat 
## Class
Foam::fileStat

## Description
Wrapper for stat() system call.

## Warning
on Linux (an maybe on others) a stat() of an nfs mounted (remote)
file does never timeout and cannot be interrupted!
So e.g. Foam::ping first and hope nfs is running.

## SourceFiles
fileStat.C

