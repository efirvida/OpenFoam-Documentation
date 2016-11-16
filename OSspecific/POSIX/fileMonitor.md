# fileMonitor 
## Class
Foam::fileMonitor

## Description
Checking for changes to files.

## Note
The default is to use stat to get the timestamp.

Compile with FOAM_USE_INOTIFY to use the inotify
(Linux specific, since 2.6.13) framework. The problem is that inotify does
not work on nfs3 mounted directories!!

## SourceFiles
fileMonitor.C

