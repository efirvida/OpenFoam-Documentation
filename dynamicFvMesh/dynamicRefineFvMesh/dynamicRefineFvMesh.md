# dynamicRefineFvMesh 
## Class
Foam::dynamicRefineFvMesh

## Description
A fvMesh with built-in refinement.

Determines which cells to refine/unrefine and does all in update().


        // How often to refine
        refineInterval  1;
        // Field to be refinement on
        field           alpha.water;
        // Refine field inbetween lower..upper
        lowerRefineLevel 0.001;
        upperRefineLevel 0.999;
        // If value < unrefineLevel (default=GREAT) unrefine
        //unrefineLevel   10;
        // Have slower than 2:1 refinement
        nBufferLayers   1;
        // Refine cells only up to maxRefinement levels
        maxRefinement   2;
        // Stop refinement if maxCells reached
        maxCells        200000;
        // Flux field and corresponding velocity field. Fluxes on changed
        // faces get recalculated by interpolating the velocity. Use 'none'
        // on surfaceScalarFields that do not need to be reinterpolated, use
        // NaN to detect use of mapped variable
        correctFluxes
        (
            (phi none)  //NaN)   //none)
            (nHatf none)   //none)
            (rho*phi none)   //none)
            (ghf none)  //NaN)   //none)
        );
        // Write the refinement level as a volScalarField
        dumpLevel       true;


## SourceFiles
dynamicRefineFvMesh.C

