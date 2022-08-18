# Allen CCF to In Vivo Alignment

The CCF coordinates returned by this tool are not identical to the in vivo mouse brain, which creates a problem for planning surgeries. We are attempting to get around this problem in a few ways, which we explain below.

## Linear stereotaxic transforms

We know for sure that the CCF atlas is stretched along the DV axis (`in vivo = 0.952 * CCF`) and squashed on the AP axis (`in vivo = 1.087 * CCF`). In the **Atlas** settings panel you can choose a coordinate transform to implement these changes. By default, we enable the **Needles Transform** which stretches/squashes the brain as described above and sets the (0,0,0) coordinate to Bregma.

Note that there also appears to be a rotation in the lamda-bregma angle of about 7 degrees (CCF is pitched forward), we are not yet accounting for this.

## Non-linear MRI transforms

The deformation in the CCF is a result of the perfusion process and the handling of brains that occurred before imaging to create that atlas. We know we can improve on this significantly by using in vivo MRIs from mice to estimate the deformation and then apply a non-linear warp to put target coordinates back into the real live mouse brain. In addition, MRIs would provide useful information about adjusting targeting based on brain age. 

At the IBL we are considering whether to acquire individual MRIs for mice and then average these to create an improved targeting space. If you are interested in helping with this process please get in touch. 