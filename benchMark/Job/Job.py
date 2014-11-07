#!/usr/bin/python

import threading

class Job(threading.Thread):
    __jobName__ = ""
    status = ("running", "killed", "finished")

    def __init__(self):
        threading.Thread.__init__(self)

    def __clean__(self):
        pass

if __name__ == "__main__":
    print "a job"
