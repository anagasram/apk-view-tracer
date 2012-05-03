#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## ParseView.py


from GlobalVariable import *
from InitDevice import init_service
from DeviceConnection import getInfosByTelnet
import telnetlib

class ParseView():
    
    def __init__(self):
        pass
    
    #406c1d58 com.android.internal.service.wallpaper.ImageWallpaper
    #4054bf40 com.android.launcher/com.android.launcher2.Launcher
    #4073dcd8 com.example.android.apis/com.example.android.apis.ApiDemos
    #406a7510 TrackingView
    #405ec120 StatusBarExpanded
    #40632908 StatusBar
    #4067b9e8 Keyguard
    #DONE
    def isSystemView(self, view_detail):
        if "com.android.internal.service.wallpaper.ImageWallpaper" == view_detail:
            return True
        elif "com.android.launcher/com.android.launcher2.Launcher" == view_detail:
            return True
        elif "TrackingView" == view_detail:
            return True
        elif "StatusBarExpanded" ==  view_detail:
            return True
        elif "StatusBar" == view_detail:
            return True
        elif "Keyguard" == view_detail:
            return True
        else:
            return False
    
    def parseViewListData(self, view_list_data):
        viewListHashCode_List = []
        viewListHashCode_Dict = {}
        lines_list = view_list_data.split("\n")
        if '' in lines_list:
            lines_list.remove('')
        if 'DONE' in lines_list:
            lines_list.remove('DONE')
        for line in lines_list:
            temp = line.split(" ")
            hashcode = temp[0]
            detail_info = temp[1]
            # clear the views of android system default services or applications
            # ImageWallpaper,Launcher,TrackingView,StatusBarExpanded,StatusBar,Keyguard
            if not self.isSystemView(detail_info):
                viewListHashCode_List.append(hashcode)
                viewListHashCode_Dict[hashcode] = detail_info
    
        print viewListHashCode_List
        return viewListHashCode_List, viewListHashCode_Dict


def GetMoreInfos():
    # List View and get Current Focus
    if False == init_service():
        print "failed to init service!"
        return False
        #return None
    
    tn = telnetlib.Telnet(host, port, time_out)
    tn.write("GET_FOCUS\n")
    CurView_Data = tn.read_until("DONE")
    tn.close()
    tn = telnetlib.Telnet(host, port, time_out)
    tn.write("LIST\n")
    ViewList_Data = tn.read_until("DONE")
    tn.close()
    print "Current Focused Window:"    
    view_parser = ParseView()
    print CurView_Data
    view_parser.parseViewListData(CurView_Data)
    print "Current Windows List:"
    print ViewList_Data
    view_parser.parseViewListData(ViewList_Data)
    
    return CurView_Data, ViewList_Data

#===========================================================================
# # these two files are same, (sha1 are same)
# # so "dump -1" means "dump %s" %focused_view_hashcode
#===========================================================================
def test():
    tn = telnetlib.Telnet(host, port, time_out)
    tn.write("DUMP -1\n")
    default_dump_data = tn.read_until("DONE")
    tn.close()
    f=open("default_dump_data", "w")
    f.write(default_dump_data)
    f.close()
    
    t = GetMoreInfos()[0]
    parser = ParseView()
    ViewHashCode = parser.parseViewListData(t)[0][0]  ## focused view hash code
    tn = telnetlib.Telnet(host, port, time_out)
    tn.write("DUMP %s\n" %ViewHashCode)
    assign_dump_data = tn.read_until("DONE")
    tn.close()
    f=open("assign_dump_data", "w")
    f.write(assign_dump_data)
    f.close()

def DiffCheck_Views():
    Infos = GetMoreInfos()
    curViewData = Infos[0]
    viewListData = Infos[1]

if __name__=="__main__":
    test()
    DiffCheck_Views()
    
