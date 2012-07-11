#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## ViewServerCommand.py

from DeviceManagement import Device

class ViewServerCommand():
    '''
    View Server Command
    '''
    
    list_view_cmd = "LIST"
    dump_view_cmd = "DUMP"
    server_cmd = "SERVER"
    protocol_cmd = "PROTOCOL"
    get_focus_cmd = "GET_FOCUS"
    autolist_cmd = "AUTOLIST"
    
    # ViewDebug Command
    capture_cmd = "CAPTURE"
    invalidate_cmd = "INVALIDATE"
    profile_cmd = "PROFILE"
    
    def __init__(self, logger):
        self.class_name = "DeviceCommand"
        self.m_logger = logger
        self.device_manager = Device(self.m_logger)
        
        if not self.device_manager.init_device():
            return False
    
    #===========================================================================
    # # ViewServer Command
    #===========================================================================
    
    # get ViewServer server version
    def getServerInfo(self):
        return self.device_manager.getInfosByTelnet(ViewServerCommand.server_cmd)
    
    # get ViewServer protocol version
    def getProtocolInfo(self):
        return self.device_manager.getInfosByTelnet(ViewServerCommand.protocol_cmd)
    
    # get View Info of Current Focused Window     
    def getFocusViewInfo(self):
        return self.device_manager.getInfosByTelnet(ViewServerCommand.get_focus_cmd)
    
    def getFocusViewHashCode(self):
        info = self.getFocusViewInfo()
        currentView = info.split("\n")[0]
        hash_code = currentView.split(" ")[0]
        return hash_code        
    
    def getViewListInfo(self):
        return self.device_manager.getInfosByTelnet(ViewServerCommand.list_view_cmd)
    
    # current view is focused view
    def getCurrentViewInfo(self):
        dump_command = ViewServerCommand.dump_view_cmd + " -1"
        return self.device_manager.getInfosByTelnet(dump_command)

    def dumpViewInfosByHashCode(self, hash_code="-1"):
        dump_command = ViewServerCommand.dump_view_cmd + " " + str(hash_code)
        try:
            return self.device_manager.getInfosByTelnet(dump_command)
        except Exception, e:
            msg = "[%s]: Failed to Dump this view. The ID might be invalid! [%s]" %(self.class_name, str(e))
            print msg
            self.m_logger.error(msg)
            return None
    
    # this method might have problem
    def getAutoListInfo(self):
        return self.device_manager.getInfosByTelnet(ViewServerCommand.autolist_cmd)


#------------------------------------------------------------------------------ 
    #===========================================================================
    # # ViewDebug Command; they are retained for testing 
    #===========================================================================
    
    def captureInfoByHashCode(self, hash_code):
        capture_command = ViewServerCommand.capture_cmd + " " + str(hash_code)
        try:
            return self.device_manager.getInfosByTelnet(capture_command)
        except Exception,e:
            msg = "[ERROR]:" + "Failed to Capture this view. The ID might be invalid! [%s]" %str(e)
            print msg
            self.m_logger.error(msg)
            return None
        
    def invalidateInfoByID(self, strID):
        invalidate_command = ViewServerCommand.invalidate_cmd + " " + str(strID)
        try:
            return self.device_manager.getInfosByTelnet(invalidate_command)
        except Exception,e:
            msg = "[ERROR]:" + "Failed to Invalidate this view. The ID might be invalid! [%s]" %str(e)
            print msg
            self.m_logger.error(msg)
            return None
        
    def profileInfoByID(self, strID):
        profile_command = ViewServerCommand.profile_cmd + " " + str(strID)
        try:
            return self.device_manager.getInfosByTelnet(profile_command)
        except Exception,e:
            msg = "[ERROR]:" + "Failed to Profile this view. The ID might be invalid! [%s]" %str(e)
            print msg
            self.m_logger.error(msg)
            return None
#------------------------------------------------------------------------------ 

if __name__ == "__main__":
    deviceCmd = ViewServerCommand()
#    deviceCmd.getViewListInfo()
    deviceCmd.captureInfoByID("406a4c68")
    deviceCmd.invalidateInfoByID("406a4c68")
    deviceCmd.profileInfoByID("406a4c68")
    
    