#
# stub function definition file for docstring parsing
#

def sdpolaverage(infile, datacolumn='data', antenna='', field='', spw='', timerange='', scan='', intent='', polaverage='', outfile=''):
    r"""
Average SD spectra over polarisation

Parameters
   - infile_ (string) - name of input SD dataset
   - datacolumn_ (string='data') - name of data column to be used ["data", "float_data", or "corrected_data"]
   - antenna_ (string='') - select data by antenna name or ID, e.g. "PM03"
   - field_ (string='') - select data by field IDs and names, e.g. "3C2*" (""=all)
   - spw_ (string='') - select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)
   - timerange_ (string='') - select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
   - scan_ (string='') - select data by scan numbers, e.g. "21~23" (""=all)
   - intent_ (string='') - select data by observational intent, e.g. "*ON_SOURCE*" (""=all)
   - polaverage_ (string='') - polarization averaging mode ("", "stokes" or "geometric").
   - outfile_ (string='') - name of output file


Description
   Task **sdpolaverage** is used to export Single Dish MS data
   averaged over different polarizations, to obtain Stokes I from
   orthogonal autocorrelation pairs (XXYY/LLRR).

   .. rubric:: Polarization Average
      

   Two modes of polarizaton averaging are available. One is 'stokes'
   which is an average based on a formulation of Stokes parameter. In
   this mode, averaged data is calculated by (XX + YY) / 2 or (RR +
   LL) / 2. The other option is 'geometric', which is a conventional
   way of averaging in the field of single-dish data reduction; the
   output data is given by weighted average of XX and YY, or RR and
   LL.




Details
   Explanation of each parameter

.. _infile:

   .. rubric:: infile

   | name of input SD dataset

.. _datacolumn:

   .. rubric:: datacolumn

   | name of data column to be used ["data", "float_data", or "corrected_data"]

.. _antenna:

   .. rubric:: antenna

   | select data by antenna name or ID, e.g. "PM03"

.. _field:

   .. rubric:: field

   | select data by field IDs and names, e.g. "3C2*" (""=all)

.. _spw:

   .. rubric:: spw

   | select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)

.. _timerange:

   .. rubric:: timerange

   | select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)

.. _scan:

   .. rubric:: scan

   | select data by scan numbers, e.g. "21~23" (""=all)

.. _intent:

   .. rubric:: intent

   | select data by observational intent, e.g. "*ON_SOURCE*" (""=all)

.. _polaverage:

   .. rubric:: polaverage

   | polarization averaging mode ("", "stokes" or "geometric").

.. _outfile:

   .. rubric:: outfile

   | name of output file


    """
    pass