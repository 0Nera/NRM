import os, sys, platform, site, getpass, socket, psutil, pyautogui
from uuid import getnode as get_mac
from datetime import datetime
from PIL import Image
from os.path import join


print("Current OS variables as seen by Python3 (%s)" % platform.python_version() )

print('USER:                %s' % getpass.getuser())
print('TIME:                %s' % datetime.fromtimestamp(psutil.boot_time()))

print('MAC:                 %s' % get_mac())
print('IP:                  %s' % socket.gethostbyname(socket.getfqdn()))

print('CPU:                 %s' % str(psutil.cpu_freq()))

print('os.getenv(\"TERM\"):   %s' % os.getenv("TERM"))   # [xterm, xterm-color, xterm-256color]
print('os.name:             %s' % os.name )              # [posix, nt, java]
print('os.sys.platform:     %s' % os.sys.platform )      # [linux, win32, cygwin, darwin]
print('sys.platform:        %s' % sys.platform )         # [linux, win32, cygwin, darwin]


try:
    print('\tnodename:      %s' % os.uname()[1] )   #
    print('\tmachine:       %s' % os.uname()[4] )   #
    print('\tsysname:       %s' % os.uname()[0] )   #
    print('\trelease:       %s' % os.uname()[2] )   #
    print('\tversion:       %s' % os.uname()[3] )   #
except:
    pass


#os.system("cmd.exe")
print('Fuck')

screen = pyautogui.screenshot("screenshot.jpg") # Снятие скриншота