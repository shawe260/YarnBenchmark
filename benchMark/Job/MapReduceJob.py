#!/usr/bin/python

import time
import subprocess
from Job import Job

#should parse conifguration file to get the job specification
class MapReduceJob(Job):
    
    def __init__(self, name):
        #The super is needed to start a thread
        super(MapReduceJob, self).__init__()
        self.__jobName = name;

    def run(self):
        print "Starting a MapReduce Job: " + self.__jobName
        start = time.time()
        print "Start time: " + time.ctime(start);
        '''DIR = "/usr/local/Hadoop2.0/hadoop-2.4.1/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.4.1.jar"
        d = subprocess.Popen(["yarn", "jar", DIR, "teragen", "100000", "/tera1"],
        stdout = subprocess.PIPE, stderr = subprocess.PIPE);
        
        dc = d.communicate()
        print dc[0]'''
        time.sleep(37)
        end = time.time()
        print "\nMapReduce Job: " + self.__jobName + "finished with status <Succeeded>"
        print "End time: " + time.ctime(end);
        print "Elapsed: " + str(end - start);


if __name__ == "__main__":
    print "MapReduce Job"
    m = MapReduceJob('Randomwritor')
    m.start()
