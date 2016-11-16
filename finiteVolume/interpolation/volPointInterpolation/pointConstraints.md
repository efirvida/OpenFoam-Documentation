# pointConstraints 
## Class
Foam::pointConstraints

## Description
Application of (multi-)patch point contraints.

Note: includes all points which are on the boundary of a patch
          with a constraint. It includes them (even though the constraint
          will already be implemented through the patch evaluation)
          since these points might be
          coupled to points which are not on any constraint patch and we
          don't want to get inconsistency between the two points.

## SourceFiles
pointConstraints.C
pointConstraintsTemplates.C

