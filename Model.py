#!/usr/bin/python

# Data to be displayed on the app
from Configuration.Models import Linux_OS_Release, Linux_Check, SW_Check

class Model_OSRelease:
    def __init__(self, parent):
        self.MVC_App = parent.MVC_App
        self.App_Sys = parent.App_sys
        self.OS_Info = Linux_OS_Release.OS_Release()
        self.SW_Info = SW_Check.SW_Installed(self)
        print("Information Gathered")

    def Test_OS(self):
        print("PRETTY_NAME = " + self.OS_Info.PRETTY_NAME)
        print("NAME = " + self.OS_Info.NAME)
        print("VERSION_ID = " + self.OS_Info.VERSION_ID)
        print("VERSION = " + self.OS_Info.VERSION)
        print("VERSION_CODENAME = " + self.OS_Info.VERSION_CODENAME)
        print("ID = " + self.OS_Info.ID)
        print("ID_LIKE = " + self.OS_Info.ID_LIKE)
        print("HOME_URL = " + self.OS_Info.HOME_URL)
        print("SUPPORT_URL = " + self.OS_Info.SUPPORT_URL)
        print("BUG_REPORT_URL = " + self.OS_Info.BUG_REPORT_URL)
