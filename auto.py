#!/usr/bin/python
__author__ = 'jjj'
# -*- coding:utf8 -*-
import subprocess
import datetime
import shlex
import time
datestring = str(datetime.datetime.now())

class Auto:
    # make some difference everyday
    def make_some_different(self):
        with open("./shit", "a") as f:
            f.write(datestring)
    def main(self):
        self.make_some_different()
        cmd = "git add -u"
        subprocess.Popen(shlex.split(cmd))
	time.sleep(1)
        cmd = "git commit -m '{0}'".format(datestring)
        subprocess.Popen(shlex.split(cmd))
	time.sleep(1)
        cmd = "git push origin master"
        subprocess.Popen(shlex.split(cmd))

if __name__ == "__main__":
    fucker = Auto()
    while True:
        fucker.main()
	time.sleep(10)
