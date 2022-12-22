# in vivo Alignment

The Allen Common Coordinate Framework was defined using perfused brains, which are warped compared to the *in vivo* mouse brain inside the skull. To improve the accuracy of targeting we attempt to un-warp the CCF by using an *in vivo* transform. There are currently three transforms available by default in Pinpoint. You can enable the different Atlas options by navigating to the Atlas menu and selecting the option from the dropdown list.

We recommend using the default MRI transform, but other options are available and the warping can be turned off.

## Linear transforms

The linear transforms implement linear scaling and rotation.

### CCF Atlas

If you prefer to plan your trajectories in the CCF space without a transformation choose the "CCF Atlas" option. Note that the CCF has a known pitch of at least 5 degrees relative to a skull where bregma and lambda have been leveled.

### Paxinos Atlas

Coming soon...

### Toronto MRI transform

The Toronto MRI transform is based on an average MRI image from 12 p65 C57BL/6j mice that were alive at the time of scanning. The MRI volume was aligned to the CCF to estimate the warping function. The result was:

`in vivo = (1.031 * ap, 0.952 * ml, 0.885* dv)`

We also know from the IBL reproducible ephys paper that the CCF atlas is pitched down by about 5 degrees relative to a flat skull (where bregma and lambda are at the same DV height). To account for this we implement a rotation:

`in vivo (yaw,pitch,spin) = (+0, -5, +0)`

Please see [the MRI paper](https://www.nature.com/articles/s41467-018-04921-2) and the [reproducible ephys paper](https://www.biorxiv.org/content/10.1101/2022.05.09.491042v3) for additional details.

### Needles transform

The Needles atlas transform is based on average MRI image from 40 p84 mice taken post-mortem but still in the skull. The result was:

`in vivo = (1.087 * ap, 1.000 * ml, 0.952 * dv)`

`in vivo (yaw,pitch,spin) = (+0, -5, +0)`

Please see [the MRI paper](https://pubmed.ncbi.nlm.nih.gov/18502665/) for details.

### IBL Needles transform

The IBL Needles atlas is the same transform without the pitch rotation. It is only included for legacy purposes and is not recommended.

## Non-Linear Transforms

Coming soon...