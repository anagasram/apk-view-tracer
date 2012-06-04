#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## testMonkeyRunnerImpl.py

import os,sys
curDir=os.getcwd()
sys.path.append(curDir)

from MonkeyRunnerImpl import MonkeyRunnerImpl

def touchEventByViewPointList(view_point_list,monkey_runner_impl):
    for view_point in view_point_list:
        monkey_runner_impl.touch(view_point[0],view_point[1],"DOWN_AND_UP")    

def main():
    monkey_runner_impl = MonkeyRunnerImpl()
    view_file_dir = os.getcwd() + os.sep + "view_file"
    view_file_path = view_file_dir + os.sep + "click.vf"
    view_file = open(view_file_path, "r")
    view_point_list=[]
    for eachline in view_file:
        l = eachline.strip("\n").split("|")
        t = (int(l[0],10),int(l[1],10))
        view_point_list.append(t)
      

    touchEventByViewPointList(view_point_list,monkey_runner_impl)

if __name__ == "__main__":
    print "begin main"
    main()
    print "end main"