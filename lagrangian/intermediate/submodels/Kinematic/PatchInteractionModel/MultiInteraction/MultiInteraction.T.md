# MultiInteraction.T 
## Class
Foam::MultiInteraction

## Description
Runs multiple patch interaction models in turn. Takes dictionary
where all the subdictionaries are the interaction models.

        // Exit upon first successful interaction or continue doing other
        // models. Returned nteraction status will be true if there has been any
        // interaction (so logical or)
        oneInteractionOnly true;

        model1
        {
            patchInteractionModel coincidentBaffleInteraction;
            coincidentBaffleInteractionCoeffs
            {
                coincidentPatches
                (
                    (pipetteWall_A pipetteCyclic_half0)
                    (pipetteWall_B pipetteCyclic_half1)
                );
            }
        }
        model2
        {
            patchInteractionModel localInteraction;
            localInteractionCoeffs
            {
                patches
                (
                    cWall
                    {
                        type rebound;
                    }
                    pipetteWall_A
                    {
                        type rebound;
                    }
                    pipetteWall_B
                    {
                        type rebound;
                    }
                );
            }
        }


