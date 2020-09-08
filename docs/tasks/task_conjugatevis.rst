Description
   This task changes the sign of the phases in all visibility
   columns, thus creating the complex conjugate values. A complex
   number and its complex conjugate have equal real parts and
   imaginary parts that are equal in magnitude but opposite in sign.

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: vis
      

   Name of input visibility file. For example: *vis='filename.ms'*

   .. rubric:: spwlist
      

   Selects spectral window(s). For example: *spw=[1,2]*. By default,
   all spws will be conjugated.

   .. rubric:: outputvis
      

   Name of output visibility file. Default:
   'conjugatedvis_filename.ms'

   .. rubric:: overwrite
      

   Overwrites the *outputvis* if it exists. Default=False