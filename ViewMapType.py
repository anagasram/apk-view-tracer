#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## ViewMapType.py

## View Map 
class CViewMapElement(object):
    def __init__(self):
        self.mHashCode = "12345678"              ## hex string <Hash Code of WindowState Object>
        self.mTriggerHashCode = "12345678"       ## same as above
        self.mNextElementHashCode= "12345678"    ## same as above