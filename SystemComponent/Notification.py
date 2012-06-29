#! python2.7
## -*- coding: utf-8 -*-

#===============================================================================
# @author: kun
# @date: 2012-06-27
#===============================================================================


class Notification():
    '''
    Operate Android Notification 
    '''
    
    def __init__(self, dump_info):
        self.statusbar_top = 0
        self.statusbar_bottom = 37
        self.statusbar_left = 8
        self.statusbar_right = 471
        
        self.view_info = dump_info
        
        self.carrierlabel_class_name = "com.android.systemui.statusbar.CarrierLabel"
        self.ongoing_class_name = ""
        self.notifications_class_name = ""
        
        self.item_class_name = 'com.android.systemui.statusbar.LatestItemView'
        
    
    def callNotification(self):
        pass
    
    def getCarrierInfo(self):
        pass
    
    # mText : Clear
    # mId : clear_all_button
    def getClearButtonLocation(self):
        pass
    
    def getOngoingList(self):
        pass
    
    def getNotificationList(self):
        pass
    
    