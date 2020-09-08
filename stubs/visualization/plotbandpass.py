#
# stub function definition file for docstring parsing
#

def plotbandpass(caltable, antenna='', field='', spw='', yaxis='amp', xaxis='chan', figfile='', plotrange=[0,0,0,0], caltable2='', overlay='', showflagged=False, timeranges='', buildpdf=False, caltable3='', markersize=3, density=108, interactive=True, showpoints='auto', showlines='auto', subplot='22', zoom='', poln='['']', showatm=False, pwv='auto', gs='gs', convert='convert', chanrange='', solutionTimeThresholdSeconds=30.0, debug=False, phase='['']', vis='', showtsky=False, showfdm=False, showatmfield='', lo1='', showimage=False, showatmpoints=False, parentms='', pdftk='pdftk', channeldiff=False, edge=8, resample=1, platformingThreshold=10.0, platformingSigma=10.0, basebands='', showBasebandNumber=False, scans='', figfileSequential=False, chanrangeSetXrange=False):
    r"""
Makes detailed plots of Tsys and bandpass solutions.

Parameters
   - caltable_ (string) - Input table name, either a bandpass solution or a Tsys solution
   - antenna_ ({string, int, stringArray, intArray}='') - A comma-delimited string list of antennas (either names or integer indices) for which to display solutions.  Default = all antennas.
   - field_ ({string, int, stringArray, intArray}='') - A comma-delimited string list of fields (either names or integer indices) for which to display solutions.  Default = all fields.
   - spw_ ({string, int, stringArray, intArray}='') - A comma-delimited string list of spws for which to display solutions.  Default = all spws.
   - yaxis_ (string='amp') - The quantity to plot on the y-axis ("amp", "phase", "both", "tsys", append "db" for dB).

      .. raw:: html

         <details><summary><i> yaxis = both </i></summary>

      - phase_ ({intArray, string}='['']') - The y-axis limits to use for phase plots when yaxis="both"

      .. raw:: html

         </details>
   - xaxis_ (string='chan') - The quantity to plot on the x-axis ("chan" or "freq").

      .. raw:: html

         <details><summary><i> xaxis = freq </i></summary>

      - chanrange_ ({string, intArray}='') - Set xrange ("5~100") over which to autoscale y-axis for xaxis="freq"
      - showfdm_ (bool=False) - when showing TDM spws, draw the locations of the corresponding FDM spws
      - chanrangeSetXrange_ (bool=False) - If True, then chanrange also sets the xrange to display

      .. raw:: html

         </details>
   - figfile_ (string='') - The name of the plot file to produce.
   - plotrange_ (doubleArray=[0,0,0,0]) - The axes limits to use [x0,x1,y0,y1].
   - caltable2_ (string='') - A second cal table, of type BPOLY or B, to overlay on a B table
   - overlay_ (string='') - Show multiple solutions in same frame in different colors (time, antenna, spw, baseband, or time,antenna)

      .. raw:: html

         <details><summary><i> overlay = time </i></summary>

      - showatmfield_ ({int, string}='') - for overlay="time", use first observation of this fieldID or name

      .. raw:: html

         </details>
   - showflagged_ (bool=False) - Show the values of the solution, even if flagged
   - timeranges_ (string='') - Show only these timeranges, the first timerange being 0
   - markersize_ (int=3) - Size of points
   - interactive_ (bool=True) - if False, then run to completion automatically without pause
   - showpoints_ ({string, bool}='auto') - Draw points for the data (default=F for amp, T for phase)
   - showlines_ ({string, bool}='auto') - Draw lines connecting the data (default=T for amp, F for phase)
   - subplot_ ({string, int}='22') - 11..81,22,32 or 42 for RowsxColumns (default=22), any 3rd digit is ignored
   - poln_ ({stringArray, string}='['']') - Polarizations to plot: "" = all, or "RR","RL","LR","LL","XX","XY","YX","YY","RR,LL","XX,YY"
   - showatm_ (bool=False) - Compute and overlay the atmospheric transmission curve
   - solutionTimeThresholdSeconds_ (double=30.0) - Consider 2 solutions simultaneous if within this interval in seconds
   - debug_ (bool=False) - Print verbose messages for debugging purposes
   - vis_ (string='') - name of the ms for this table, in case it does not match the string in the caltable
   - showtsky_ (bool=False) - Compute and overlay the sky temperature curve instead of transmission
   - channeldiff_ ({bool, double}=False) - Set to a value > 0 (sigma) to plot derivatives of the solutions
   - basebands_ ({int, string, intArray}='') - A baseband number or list of baseband numbers for which to display solutions.  Default = all.
   - showBasebandNumber_ (bool=False) - Put the baseband converter number (BBC_NO) in the title of each plot
   - scans_ ({int, string, intArray}='') - A scan or list of scans for which to display solutions.  Default = all. Does not work with overlay="time".
   - figfileSequential_ (bool=False) - naming scheme for pngs: False: name by spw/antenna (default), True: figfile.000.png, figfile.001.png, etc.


Description
   .. rubric:: Summary
      

   Plots the bandpass and system temperature (T sys) solutions.

   This generic task was developed at the North American ALMA Science
   Center (NAASC). It displays T sys and bandpass solution tables
   with options to overlay them in variouscombinations, and/or with
   an atmospheric transmission or sky temperaturemodel. It allows
   for mixed-mode spws (e.g., TDM and FDM for ALMA) and uses the msmd
   tool to access the information about an MS.

   Note thatthe ability to compute and overlay an atmospheric
   transmission curve or a sky temperature curve is now also
   available in **plotms**.

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: *antenna*
      

   Must be either an ID (int or string or list), or a single antenna
   name or list.

   .. rubric:: *basebands*
      

   Show only spws from the specified baseband or list of basebands
   (default: ''=[]=all)

   .. rubric:: buildpdf
      

   True/False; if True and figfile is set, assemble pngs into a pdf

   .. rubric:: caltable
      

   A bandpass table, of type B or BPOLY

   .. rubric:: *caltable2*
      

   A second cal table, of type BPOLY or B, to overlay on a B table

   .. rubric:: *caltable3*
      

   A third cal table, of type BPOLY, to overlay on the first two

   .. rubric:: channeldiff
      

   Set to value > 0 to plot derivatives of amplitude. The value is
   also used as sigma, and any outliers beyond this sigma will be
   printed to the logger

   .. rubric:: *chanrange*
      

   set xrange over which to autoscale y-axis for xaxis='freq' (e.g.,
   "5~100")

   .. rubric:: *chanrangeSetXrange*
      

   If True, then chanrange also sets the xrange to display

   .. rubric:: *convert*
      

   Full path for convert command (in case it's not found)

   .. rubric:: *density*
      

   Dpi to use in creating PNGs and PDFs (default=108)

   .. rubric:: *edge*
      

   The number of edge channels to ignore in finding outliers (for
   channeldiff>0)

   .. rubric:: *field*
      

   must be an ID, source name, or list thereof; can use trailing \*:
   'J*'

   .. rubric:: *figfile*
      

   The base_name of the png files to save: base_name.antX.spwY.png

   .. rubric:: figfileSequential
      

   Naming scheme. False: name by spw/antenna (default).True:
   figfile.1.png, figfile.2.png, etc.

   .. rubric:: *gs*
      

   Full path for ghostscript command (in case it's not found)

   .. rubric:: *interactive*
      

   If False, then figfile will run to completion automatically

   .. rubric:: *lo1*
      

   Specify the LO1 setting (in GHz) for the observation

   .. rubric:: overlay
      

   Overlay 'antenna','time','spw', or 'baseband'; make 1 plot with
   different items in colors

   .. rubric:: *markersize*
      

   Size of points (default=3)

   .. rubric:: ms
      

   Name of the ms for this table, in case it does not match the
   string in the caltable

   .. rubric:: *parentms*
      

   Name of the parent ms, in case the ms has been previously split

   .. rubric:: *pdftk*
      

   Full path for pdftk command (in case it's not found)

   .. rubric:: *phase*
      

   The y-axis limits to use for phase plots when yaxis='both'

   .. rubric:: *platformingSigma*
      

   Declare platforming if the amplitude derivative exceeds this many
   times the MAD

   .. rubric:: *platformingThreshold*
      

   If *platformingSigma=0*, then declare platforming if the amplitude
   derivative exceeds this percentage of the median

   .. rubric:: *plotrange*
      

   Define axis limits: [x0,x1,y0,y1] where 0,0 means auto

   .. rubric:: *poln*
      

   Polarizations to plot (e.g., 'XX','YY','RR','LL' or '' for both)

   .. rubric:: *pwv*
      

   Define the precipitable water vapour(pwv) to use for the showatm
   option: 'auto' or value in mm

   .. rubric:: *resample*
      

   Channel expansion factor to use when computing MAD of derivative
   (for channeldiff>0)

   .. rubric:: *scans*
      

   Show only solutions for the specified scans (int, list, or string)

   .. rubric:: *showatm*
      

   Compute and overlay the atmospheric transmission curve (on B or
   T sys solutions)

   .. rubric:: *showatmfield*
      

   Use first observation of this fieldID or name

   .. rubric:: *showatmPoints*
      

   Draw atmospheric curve with points instead of a line

   .. rubric:: *showBasebandNumber*
      

   Put the BBC_NO in the title of each plot

   .. rubric:: *showfdm*
      

   When showing TDM spws with xaxis='freq', draw locations of FDM
   spws

   .. rubric:: *showflagged*
      

   Show the values of data, even if flagged

   .. rubric:: *showimage*
      

   Also show the atmospheric curve for the image sideband (in black)

   .. rubric:: *showtsky*
      

   Compute and overlay the sky temperature curve instead of
   transmission

   .. rubric:: *showlines*
      

   Draw lines connecting the data (default=True for amp, False for
   phase)

   .. rubric:: *showpoints*
      

   Draw points for the data (default=False for amp, True for phase)

   .. rubric:: *solutionTimeThresholdSeconds*
      

   Consider 2 solutions simultaneously if within this interval
   (default=60)

   .. rubric:: *spw*
      

   Must be single ID or list or range (e.g., "0~4", not the original
   ID)

   .. rubric:: *subplot*
      

   11..81,22,32 or 42 for RowsxColumns (default=22), any 3rd digit is
   ignored

   .. rubric:: *timeranges*
      

   Show only these timeranges, the first timerange being 0

   .. rubric:: *xaxis*
      

   'chan' or 'freq'

   .. rubric:: *yaxis*
      

   'amp', 'tsys', 'phase', or 'both' amp+phase == 'ap'. Append 'db'
   for dB

   .. rubric:: *zoom*
      

   'intersect' will zoom to overlap region of caltable with caltable2




Details
   Explanation of each parameter

.. _caltable:

   .. rubric:: caltable

   | Input table name, either a bandpass solution or a Tsys solution

.. _antenna:

   .. rubric:: antenna

   | A comma-delimited string list of antennas (either names or integer indices) for which to display solutions.  Default = all antennas.

.. _field:

   .. rubric:: field

   | A comma-delimited string list of fields (either names or integer indices) for which to display solutions.  Default = all fields.

.. _spw:

   .. rubric:: spw

   | A comma-delimited string list of spws for which to display solutions.  Default = all spws.

.. _yaxis:

   .. rubric:: yaxis

   | The quantity to plot on the y-axis ("amp", "phase", "both", "tsys", append "db" for dB).

.. _xaxis:

   .. rubric:: xaxis

   | The quantity to plot on the x-axis ("chan" or "freq").

.. _figfile:

   .. rubric:: figfile

   | The name of the plot file to produce.

.. _plotrange:

   .. rubric:: plotrange

   | The axes limits to use [x0,x1,y0,y1].

.. _caltable2:

   .. rubric:: caltable2

   | A second cal table, of type BPOLY or B, to overlay on a B table

.. _overlay:

   .. rubric:: overlay

   | Show multiple solutions in same frame in different colors (time, antenna, spw, baseband, or time,antenna)

.. _showflagged:

   .. rubric:: showflagged

   | Show the values of the solution, even if flagged

.. _timeranges:

   .. rubric:: timeranges

   | Show only these timeranges, the first timerange being 0

.. _buildpdf:

   .. rubric:: buildpdf

   | If True, assemble all the pngs into a pdf

.. _caltable3:

   .. rubric:: caltable3

   | A third cal table, of type BPOLY, to overlay on the first two tables

.. _markersize:

   .. rubric:: markersize

   | Size of points

.. _density:

   .. rubric:: density

   | dpi to use in creating PNGs and PDFs (default=108)

.. _interactive:

   .. rubric:: interactive

   | if False, then run to completion automatically without pause

.. _showpoints:

   .. rubric:: showpoints

   | Draw points for the data (default=F for amp, T for phase)

.. _showlines:

   .. rubric:: showlines

   | Draw lines connecting the data (default=T for amp, F for phase)

.. _subplot:

   .. rubric:: subplot

   | 11..81,22,32 or 42 for RowsxColumns (default=22), any 3rd digit is ignored

.. _zoom:

   .. rubric:: zoom

   | "intersect" will zoom to overlap region of caltable with caltable2

.. _poln:

   .. rubric:: poln

   | Polarizations to plot: "" = all, or "RR","RL","LR","LL","XX","XY","YX","YY","RR,LL","XX,YY"

.. _showatm:

   .. rubric:: showatm

   | Compute and overlay the atmospheric transmission curve

.. _pwv:

   .. rubric:: pwv

   | Define the pwv to use for the showatm option: "auto" or value in mm

.. _gs:

   .. rubric:: gs

   | For buildpdf=T, full path for ghostscript command (in case it is not found)

.. _convert:

   .. rubric:: convert

   | For buildpdf=T, full path for the ImageMagick convert command (in case it is not found)

.. _chanrange:

   .. rubric:: chanrange

   | Set xrange ("5~100") over which to autoscale y-axis for xaxis="freq"

.. _solutionTimeThresholdSeconds:

   .. rubric:: solutionTimeThresholdSeconds

   | Consider 2 solutions simultaneous if within this interval in seconds

.. _debug:

   .. rubric:: debug

   | Print verbose messages for debugging purposes

.. _phase:

   .. rubric:: phase

   | The y-axis limits to use for phase plots when yaxis="both"

.. _vis:

   .. rubric:: vis

   | name of the ms for this table, in case it does not match the string in the caltable

.. _showtsky:

   .. rubric:: showtsky

   | Compute and overlay the sky temperature curve instead of transmission

.. _showfdm:

   .. rubric:: showfdm

   | when showing TDM spws, draw the locations of the corresponding FDM spws

.. _showatmfield:

   .. rubric:: showatmfield

   | for overlay="time", use first observation of this fieldID or name

.. _lo1:

   .. rubric:: lo1

   | specify the LO1 setting (in GHz) for the observation ('' = automatic)

.. _showimage:

   .. rubric:: showimage

   | also show the atmospheric curve for the image sideband (in black)

.. _showatmpoints:

   .. rubric:: showatmpoints

   | Draw atmospheric curve with points instead of a line

.. _parentms:

   .. rubric:: parentms

   | if showimage=T, name of the parent ms (only needed if the ms has been previously split)

.. _pdftk:

   .. rubric:: pdftk

   | For buildpdf=T, full path for pdftk command (in case it is not found)

.. _channeldiff:

   .. rubric:: channeldiff

   | Set to a value > 0 (sigma) to plot derivatives of the solutions

.. _edge:

   .. rubric:: edge

   | The number of edge channels to ignore in finding outliers (for channeldiff>0)

.. _resample:

   .. rubric:: resample

   | The channel expansion factor to use when computing MAD of derivative (for channeldiff>0)

.. _platformingThreshold:

   .. rubric:: platformingThreshold

   | if platformingSigma=0, then declare platforming if the amplitude derivative exceeds this percentage of the median

.. _platformingSigma:

   .. rubric:: platformingSigma

   | declare platforming if the amplitude derivative exceeds this many times the MAD

.. _basebands:

   .. rubric:: basebands

   | A baseband number or list of baseband numbers for which to display solutions.  Default = all.

.. _showBasebandNumber:

   .. rubric:: showBasebandNumber

   | Put the baseband converter number (BBC_NO) in the title of each plot

.. _scans:

   .. rubric:: scans

   | A scan or list of scans for which to display solutions.  Default = all. Does not work with overlay="time".

.. _figfileSequential:

   .. rubric:: figfileSequential

   | naming scheme for pngs: False: name by spw/antenna (default), True: figfile.000.png, figfile.001.png, etc.

.. _chanrangeSetXrange:

   .. rubric:: chanrangeSetXrange

   | If True, then chanrange also sets the xrange to display


    """
    pass