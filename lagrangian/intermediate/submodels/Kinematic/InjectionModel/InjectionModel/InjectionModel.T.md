# InjectionModel.T 
## Class
Foam::InjectionModel

## Description
Templated injection model class.

The injection model nominally describes the parcel:
- position
- diameter
- velocity
In this case, the fullyDescribed() flag should be set to 0 (false). When
the parcel is then added to the cloud, the remaining properties are
populated using values supplied in the constant properties.

If, however, all of a parcel's properties are described in the model, the
fullDescribed() flag should be set to 1 (true).


## SourceFiles
InjectionModel.C
InjectionModelNew.C

