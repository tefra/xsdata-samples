Installation of xCBL (DTD version)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Version: 3.5
Release date: 19th Nov. 2001
For more information: http://www.xcbl.org/

The DTD version of xCBL consists of individual DTD files for each 
xCBL business document.  It is still recommended that these files all
be extracted to the same directory on your system, although it is not
absolutely necessary.

The sample files available from xCBL.org need to be in the same
directory as their root document DTD they conform to when being parsed. 
They contain a line such as this at the top:

<!DOCTYPE Order SYSTEM 'Order.dtd'>

All samples will call the file of the business document, and therefore
need to be in the same directory.