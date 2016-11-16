# argList 
## Class
Foam::argList

## Description
Extract command arguments and options from the supplied
\a argc and \a argv parameters.

Sequences with "(" ... ")" are transformed into a stringList.
For example,
```
        program -listFiles \( *.txt \)
```
would create a stringList:
```
        ( "file1.txt" "file2.txt" ... "fileN.txt" )
```
The backslash-escaping is required to avoid interpretation by the shell.

Default command-line options:
      - \par -case \<dir\>
        Select a case directory instead of the current working directory
      - \par -parallel
        Specify case as a parallel job
      - \par -doc
        Display the documentation in browser
      - \par -srcDoc
        Display the source documentation in browser
      - \par -help
        Print the usage

The environment variable \b FOAM_CASE is set to the path of the
global case (same for serial and parallel jobs).
The environment variable \b FOAM_CASENAME is set to the name of the
global case.

## Note
- The document browser used is defined by the \b FOAM_DOC_BROWSER
      environment variable or the <tt>Documentation/docBrowser</tt> entry
      in the <tt>~OpenFOAM/controlDict</tt> file.
      The \%f token is used as a placeholder for the file name.
- The valid (mandatory) arguments can be adjusted
      by directly manipulating the argList::validArgs static member.
- The valid options can be adjusted
      via the addOption/removeOption static methods instead of directly
      manipulating the argList::validOptions static member.

## SourceFiles
argList.C
argListI.H

