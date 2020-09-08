#
# stub function definition file for docstring parsing
#

def imsubimage(imagename, outfile='', box='', region='', chans='', stokes='', mask='', dropdeg=False, overwrite=False, verbose=True, stretch=False, keepaxes=['']):
    r"""
Create a (sub)image from a region of the image

Parameters
   - imagename_ (string) - Input image name.  Default is unset.
   - outfile_ (string='') - Output image name.  Default is unset.
   - box_ (string='') - Rectangular region to select in direction plane. Default is to use the entire direction plane.
   - region_ (string='') - Region selection. Default is to use the full image.
   - chans_ (string='') - Channels to use. Default is to use all channels.
   - stokes_ (string='') - Stokes planes to use. Default is to use all Stokes planes.
   - mask_ (variant='') - Mask to use. Default is none.
   - dropdeg_ (bool=False) - Drop degenerate axes

      .. raw:: html

         <details><summary><i> dropdeg = True </i></summary>

      - keepaxes_ (intArray=['']) - If dropdeg=True, these are the degenerate axes to keep. Nondegenerate axes are implicitly always kept.

      .. raw:: html

         </details>
   - verbose_ (bool=True) - Post additional informative messages to the logger


Description
   This task copies all or part of the image to a new image specified
   by *outfile*. Both float and complex valued images are supported.

   Sometimes it is useful to drop axes of length one (degenerate
   axes). Set *dropdeg* equal to True if you want to do this.

   The output mask is the union (logical AND) of the default input
   pixel mask (if any) and the OTF mask. Any other input pixel masks
   will not be copied. Use function **ia.maskhandler** if you need to
   copy other masks too.

   If the mask has fewer dimensions than the image and if the shape
   of the dimensions the mask and image have in common are the same,
   the mask will automatically have the missing dimensions added so
   it conforms to the image.

   If *stretch=True* and if the number of mask dimensions is less
   than or equal to the number of image dimensions and some axes in
   the mask are degenerate while the corresponding axes in the image
   are not, the mask will be stretched in the degenerate dimensions.
   For example, if the input image has shape [100, 200, 10] and the
   input mask has shape [100, 200, 1] and *stretch=True*, the mask
   will be stretched along the third dimension to shape [100, 200,
   10]. However if the mask hasshape [100, 200, 2], stretching is
   not possible and an error will result.

   

   .. rubric:: Task-specific parameters
      

   .. rubric:: *dropdeg*
      

   Exclude axes from output image if they would have a length of one
   pixel.

   .. rubric:: *verbose*
      

   Post additional informative, possibly useful, messages to the
   logger?

   .. rubric:: *keepaxes*
      

   If dropdeg=True, these are the degenerate axes to keep.
   Nondegenerate axes are implicitly always kept. Ignored if
   dropdeg=False; all axes are kept in that case.




Details
   Explanation of each parameter

.. _imagename:

   .. rubric:: imagename

   | Input image name.  Default is unset.

.. _outfile:

   .. rubric:: outfile

   | Output image name.  Default is unset.

.. _box:

   .. rubric:: box

   | Rectangular region to select in direction plane. Default is to use the entire direction plane.

.. _region:

   .. rubric:: region

   | Region selection. Default is to use the full image.

.. _chans:

   .. rubric:: chans

   | Channels to use. Default is to use all channels.

.. _stokes:

   .. rubric:: stokes

   | Stokes planes to use. Default is to use all Stokes planes.

.. _mask:

   .. rubric:: mask

   | Mask to use. Default is none.

.. _dropdeg:

   .. rubric:: dropdeg

   | Drop degenerate axes

.. _overwrite:

   .. rubric:: overwrite

   | Overwrite (unprompted) pre-existing output file?

.. _verbose:

   .. rubric:: verbose

   | Post additional informative messages to the logger

.. _stretch:

   .. rubric:: stretch

   | Stretch the mask if necessary and possible?

.. _keepaxes:

   .. rubric:: keepaxes

   | If dropdeg=True, these are the degenerate axes to keep. Nondegenerate axes are implicitly always kept.


    """
    pass
