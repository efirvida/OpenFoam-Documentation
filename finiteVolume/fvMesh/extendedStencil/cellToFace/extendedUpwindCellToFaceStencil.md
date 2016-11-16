# extendedUpwindCellToFaceStencil 
## Class
Foam::extendedUpwindCellToFaceStencil

## Description
Creates upwind stencil by shifting a centred stencil to upwind and downwind
faces and optionally removing all non-(up/down)wind faces ('pureUpwind').

Note: the minOpposedness parameter is to decide which upwind and
downwind faces to combine the stencils from. If myArea is the
local area and upwindArea
the area of the possible upwind candidate it will be included if
        (upwindArea & myArea)/magSqr(myArea) > minOpposedness
so this includes both cosine and area. WIP.

## SourceFiles
extendedUpwindCellToFaceStencil.C
extendedUpwindCellToFaceStencilTemplates.C

