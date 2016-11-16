# includeFuncEntry 
## Class
Foam::functionEntries::includeFuncEntry

## Description
Specify a functionObject dictionary file to include, expects the
functionObject name to follow with option arguments (without quotes).

Searches for functionObject dictionary file in user/group/shipped
directories allowing for version-specific and version-independent files
using the following hierarchy:
- \b user settings:
      - ~/.OpenFOAM/\<VERSION\>/caseDicts/postProcessing
      - ~/.OpenFOAM/caseDicts/postProcessing
- \b group (site) settings (when $WM_PROJECT_SITE is set):
      - $WM_PROJECT_SITE/\<VERSION\>/caseDicts/postProcessing
      - $WM_PROJECT_SITE/caseDicts/postProcessing
- \b group (site) settings (when $WM_PROJECT_SITE is not set):
      - $WM_PROJECT_INST_DIR/site/\<VERSION\>/caseDicts/postProcessing
      - $WM_PROJECT_INST_DIR/site/caseDicts/postProcessing
- \b other (shipped) settings:
      - $WM_PROJECT_DIR/etc/caseDicts/postProcessing

The optional field arguments included in the name are inserted in 'field' or
'fields' entries in the functionObject dictionary and included in the name
of the functionObject entry to avoid conflict.

Examples:
```
        #includeFunc Q
        #includeFunc components(U)
        #includeFunc mag(Ux)
        #includeFunc mag(p)
```

## See also
Foam::functionObjectList

## SourceFiles
includeFuncEntry.C

