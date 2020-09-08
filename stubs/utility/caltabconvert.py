#
# stub function definition file for docstring parsing
#

def caltabconvert(caltabold='', vis='', ptype='complex', caltabnew=''):
    r"""
Convert old-style caltables into new-style caltables.

Parameters
   - caltabold_ (string='') - Name of the old-style caltable
   - vis_ (string='') - Name of the visibility file (MS) associated with the old-style caltable.
   - ptype_ (string='complex') - Type of data in the new-format caltable ("complex" or "float"; default is "complex").
   - caltabnew_ (string='') - Name of the new-style caltable.  If not specified, the suffix ".new" is appended to the name of old-style caltable.


Description
   .. rubric:: Summary
      

   | This task converts old-style (up to CASA 3.3.0) calibration
     tables (caltables) into new-style (CASA 3.4.0 and later)
     caltables. It is provided for convenience, but if there are
     issues, it is suggested that a new-style caltable be created
     directly. The information transferred should be enough for most
     calibration purposes.*bpoly* and *gspline* versions are not
     supported.  
   |  

   .. rubric:: Parameters
      

   .. rubric:: *caltabold*
      

   Name of the old-style caltable.

   .. rubric:: *vis*
      

   Name of the visibility file (MS) associated with the old-style
   caltable.

   .. rubric:: *ptype*
      

   Type of data in the new-format caltable. Allowed values: *complex*
   (default) or *float*

   .. note:: **NOTE**: The old-style caltables do not have this information,
      so it is imperative that users get it correct. *complex* refers
      to caltables that have complex gains (e.g., produced by
      **gaincal**, **bpcal**, etc.). *float* refers to caltables that
      have real numbers, such as delays (e.g., produced by
      **gencal**).

   .. rubric:: *caltabnew*
      

   | Name of the new-style caltable. By default, the suffix *.new* is
     appended to the name of the old-style caltable.




Details
   Explanation of each parameter

.. _caltabold:

   .. rubric:: caltabold

   | Name of the old-style caltable.
   |                      Default: none
   | 
   |                         Example: caltabold='gronk.g0'

.. _vis:

   .. rubric:: vis

   | Name of the visibility file (MS) associated with the
   | old-style caltable.
   |                      Default: none
   | 
   |                         Example: 'blurp.ms'

.. _ptype:

   .. rubric:: ptype

   | Type of data in the new-format caltable.
   |                      Default: "complex"
   |                      Options: "complex" or "float"
   | 
   |                      Note: The old-style caltables do not have this
   |                      information, so it is imperative that users get
   |                      it correct.  "complex" refers to caltables that
   |                      have complex gains (e.g., produced by gaincal,
   |                      bpcal, etc.). "float" refers to caltables that
   |                      real numbers such as delays (e.g., produced by
   |                      gencal).

.. _caltabnew:

   .. rubric:: caltabnew

   | Name of the new-style caltable.  
   |                      Default: '' (the suffix ".new" is appended to the
   |                      name of old-style caltable)


    """
    pass