#!/usr/bin/python

import time
import subprocess
from Job import Job

#should parse conifguration file to get the job specification
class SparkJob(Job):
    
    def __init__(self, name):
        #The super is needed to start a thread
        super(SparkJob, self).__init__()
        self.__jobName = name;

    def run(self):
        print "Starting a Spark Job: " + self.__jobName
        start = time.time()
        print "Start time: " + time.ctime(start);
        time.sleep(9)
        end = time.time()
        print "\nSpark Job: " + self.__jobName + " finished with status <Failed>"
        print "End time: " + time.ctime(end);
        print "Elapsed: " + str(end - start);


