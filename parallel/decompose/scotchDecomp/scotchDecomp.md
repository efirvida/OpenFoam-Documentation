# scotchDecomp 
## Class
Foam::scotchDecomp

## Description
Scotch domain decomposition.
When run in parallel will collect the whole graph on to the master,
decompose and send back. Use ptscotchDecomp for proper distributed
decomposition.

Quoting from the Scotch forum, on the 2008-08-22 10:09, Francois
PELLEGRINI posted the following details:
```
RE: Graph mapping 'strategy' string

Strategy handling in Scotch is a bit tricky. In order
not to be confused, you must have a clear view of how they are built.
Here are some rules:

1- Strategies are made up of "methods" which are combined by means of
"operators".

2- A method is of the form "m{param=value,param=value,...}", where "m"
is a single character (this is your first error: "f" is a method name,
not a parameter name).

3- There exist different sort of strategies : bipartitioning strategies,
mapping strategies, ordering strategies, which cannot be mixed. For
instance, you cannot build a bipartitioning strategy and feed it to a
mapping method (this is your second error).

To use the "mapCompute" routine, you must create a mapping strategy, not
a bipartitioning one, and so use stratGraphMap() and not
stratGraphBipart(). Your mapping strategy should however be based on the
"recursive bipartitioning" method ("b"). For instance, a simple (and
hence not very efficient) mapping strategy can be :

"b{sep=f}"

which computes mappings with the recursive bipartitioning method "b",
this latter using the Fiduccia-Mattheyses method "f" to compute its
separators.

If you want an exact partition (see your previous post), try
"b{sep=fx}".

However, these strategies are not the most efficient, as they do not
make use of the multi-level framework.

To use the multi-level framework, try for instance:

"b{sep=m{vert=100,low=h,asc=f}x}"

The current default mapping strategy in Scotch can be seen by using the
"-vs" option of program gmap. It is, to date:

r
{
        job=t,
        map=t,
        poli=S,
        sep=
        (
            m
            {
                asc=b
                {
                    bnd=
                    (
                        d{pass=40,dif=1,rem=1}
                     |
                    )
                    f{move=80,pass=-1,bal=0.002491},
                    org=f{move=80,pass=-1,bal=0.002491},
                    width=3
                },
                low=h{pass=10}
                f{move=80,pass=-1,bal=0.002491},
                type=h,
                vert=80,
                rat=0.8
            }
          | m
            {
                asc=b
                {
                    bnd=
                    (
                        d{pass=40,dif=1,rem=1}
                      |
                    )
                    f{move=80,pass=-1,bal=0.002491},
                    org=f{move=80,pass=-1,bal=0.002491},
                    width=3
                },
                low=h{pass=10}
                f{move=80,pass=-1,bal=0.002491},
                type=h,
                vert=80,
                rat=0.8
            }
        )
}
```

Given that this information was written in 2008, this example strategy will
unlikely work as-is with the more recent Scotch versions. Therefore, the
steps for getting the current default strategy from within Scotch, is to do
the following steps:

<ol>
<li> Edit the file <tt>system/decomposeParDict</tt> and use the following
settings:

```
    method          scotch;

scotchCoeffs
{
        writeGraph true;
}
```
</li>

<li> Run \c decomposePar. For example, it will write a file named
         <tt>region0.grf</tt>.
</li>

<li> Now, instead of using \c gmap, run \c gpart with the following
command structure to get the default strategy:

```
gpart \<nProcs\> -vs \<grfFile\>
```

where:

<ul>
        <li> \<grfFile\> is the file that was obtained with the option
             <tt>writeGraph=true</tt>, namely <tt>region0.grf</tt>.
        </li>
        <li> \<nProcs\> is the \c numberOfSubdomains defined in the dictionary
             file.
        </li>
</ul>
</li>

<li> At the end of the execution will be shown a long string, similar to
the following example (complete line was cropped at <tt>[...]</tt>):

```
SStrat=m{asc=b{width=3,bnd=d{pass=40,dif=1,rem=0}[...],type=h}
```
</li>

<li> Edit the file <tt>system/decomposeParDict</tt> once again and add
the \c strategy entry as exemplified:

```
    method          scotch;

scotchCoeffs
{
        //writeGraph true;
        strategy "m{asc=b{width=3,bnd=d{pass=40,dif=1,rem=0}[...],type=h}";
}
```
</li>

<li> Finally, run \c decomposePar once again, to at least test if it
         works as intended.
</li>

</ol>

## Note
\c gpart can be found in the current search path by adding the respective
\c bin folder from the Scotch installation, namely by running the following
commands:

```
source $(foamEtcFile config.sh/scotch)
export PATH=$PATH:$SCOTCH_ARCH_PATH/bin
```

## SourceFiles
scotchDecomp.C

