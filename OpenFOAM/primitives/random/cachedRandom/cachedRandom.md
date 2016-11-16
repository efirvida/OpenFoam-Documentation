# cachedRandom 
## Class
Foam::cachedRandom

## Description
Random number generator.

Pre-computes and caches samples on construction, so that when sample01()
is called, the function simply returns the next (pre-computed) sample. On
reaching the last sample, the sample sequence is repeated.

Constructed using a seed and sample count. If the supplied count is
negative, no caching is performed, and a new sample is generated on each
call to sample01().

Note: the copy constructor cannot be used if count = -1.

## SourceFiles
cachedRandomI.H
cachedRandom.C
cachedRandomTemplates.C

