# includeEtcEntry 
## Class
Foam::functionEntries::includeEtcEntry

## Description
Specify an etc file to include when reading dictionaries, expects a
single string to follow.

Searches for files from user/group/shipped directories.
The search scheme allows for version-specific and
version-independent files using the following hierarchy:
- \b user settings:
      - ~/.OpenFOAM/\<VERSION\>
      - ~/.OpenFOAM/
- \b group (site) settings (when $WM_PROJECT_SITE is set):
      - $WM_PROJECT_SITE/\<VERSION\>
      - $WM_PROJECT_SITE
- \b group (site) settings (when $WM_PROJECT_SITE is not set):
      - $WM_PROJECT_INST_DIR/site/\<VERSION\>
      - $WM_PROJECT_INST_DIR/site/
- \b other (shipped) settings:
      - $WM_PROJECT_DIR/etc/

An example of the \c \#includeEtc directive:
```
        #includeEtc "etcFile"
```

The usual expansion of environment variables and other constructs is
retained.

## See also
findEtcFile, fileName, string::expand()

## SourceFiles
includeEtcEntry.C

