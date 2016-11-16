# extendedEdgeMesh 
## Class
Foam::extendedEdgeMesh

## Description

Description of feature edges and points.

Feature points are a sorted subset at the start of the overall points list:
        0 .. concaveStart_-1                : convex points (w.r.t normals)
        concaveStart_ .. mixedStart_-1      : concave points
        mixedStart_ .. nonFeatureStart_-1   : mixed internal/external points
        nonFeatureStart_ .. size-1          : non-feature points

Feature edges are the edgeList of the edgeMesh and are sorted:
        0 .. internalStart_-1           : external edges (convex w.r.t normals)
        internalStart_ .. flatStart_-1  : internal edges (concave)
        flatStart_ .. openStart_-1      : flat edges (neither concave or convex)
                                          can arise from region interfaces on
                                          flat surfaces
        openStart_ .. multipleStart_-1  : open edges (e.g. from baffle surfaces)
        multipleStart_ .. size-1        : multiply connected edges

The edge direction and feature edge and feature point adjacent normals
are stored.

## SourceFiles
extendedEdgeMeshI.H
extendedEdgeMesh.C
extendedEdgeMeshNew.C

