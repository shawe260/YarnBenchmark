#!/usr/bin/python

import time
import subprocess
import json
from defaults import *
from Job import Job

JOB_CONFIG_DIR = "../test.json"
JOB_NAME = "job.name"
JOB_JAR_NAME = "job.jar"
JOB_COMMAND = "job.command"
# HADOOP_HOME = os.gentenv("HADOOP_HOME")
# assert(HADOOP_HOME)

# Remember to check the path and the Things like hadoop home

#TODO should parse conifguration file to get the job specification
class MapReduceJob(Job):
    __jobConfig = {}

    # this was passed with a dicitionary of configs, 
    def __init__(self, config):
        #The super is needed to start a thread
        super(MapReduceJob, self).__init__()
        self.__jobConfig = config

    def run(self):
        print "Starting a MapReduce Job: " + self.__jobConfig[JOB_NAME]
        start = time.time()
        print "Start time: " + time.ctime(start)

        # This can also be extracted to the abstract class
        cmd = self.generateYarnCommand()
        stdout, stderr = self.runCommand(cmd)
        print stdout
        print stderr
        
        # Report the status, if possible, report to the metrics module
        end = time.time()
        print "\nMapReduce Job: " + self.__jobConfig[JOB_NAME] + " finished with status <Succeeded>"
        print "End time: " + time.ctime(end)
        print "Elapsed: " + str(end - start)

    def generateYarnCommand(self): 
        jobargs = self.__jobConfig[JOB_COMMAND].replace('%d', '-' + str(int(time.time())))
        cmd = "yarn jar {0}/{1} {2} {3}".format(JOB_POOL_DIR, 
                self.__jobConfig[JOB_JAR_NAME], 
                self.__jobConfig[JOB_NAME], 
                jobargs)
        return cmd

    def runCommand(self, cmd):
        print "The command to run is : " + cmd
        proc = subprocess.Popen(cmd, 
                shell = True,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE)
        out, err = proc.communicate()
        return out, err

    #should also consider cleanup
