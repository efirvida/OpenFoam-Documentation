# wordRe 
## Class
Foam::wordRe

## Description
A wordRe is a word, but can also have a regular expression for matching
words.

By default the constructors will generally preserve the argument as a
string literal and the assignment operators will use the wordRe::DETECT
compOption to scan the string for regular expression meta characters
and/or invalid word characters and react accordingly.

The exceptions are when constructing/assigning from another
Foam::wordRe (preserve the same type) or from a Foam::word (always
literal).

## Note
If the string contents are changed - eg, by the operator+=() or by
string::replace(), etc - it will be necessary to use compile() or
recompile() to synchronize the regular expression.

## SourceFiles
wordRe.C

