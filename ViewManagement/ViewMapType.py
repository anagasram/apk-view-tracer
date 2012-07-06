#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## ViewMapType.py


# because some views are created dynamic, and their Hash Code will change
# so Build View Map might be impossible 
# but as a human, we judge same view by text or something visible
class CViewMapElement(object):
    def __init__(self):
        self.mHashCode = "12345678"                     ## hex string <Hash Code of WindowState Object>
        self.mClassName = "com.android.View"            ## class name of WindowState Object
        self.mTriggerHashCode = "12345678"              ## same as above
        self.mTriggerClassName = "com.android.View"     ## same as above
        self.mNextElementHashCode= "12345678"           ## same as above
        self.mNextElementClassName = "com.android.View" ## same as above