#! /usr/bin/python

import time
from defaults import *
from Monitor import Monitor

class MetricsCollector:
    jobMetrics = [] #tuple (jobname, jobstatus, elapsedTime )
    totalTime = 0.0
    cnt = 0

# add a start time and end time
    def __init__(self):
        pass

    def reportJobFinish(self, job, jobType, arrt, status):
        self.jobMetrics.append((job, jobType, arrt, status))
        if (status != 'Killed'):
            self.totalTime += job.elapsedTime
            self.cnt += 1

    def generateReport(self):
        print "Report of this run: "
        # TODO: sort by arriving time here!
        for jobMetric in self.jobMetrics:
            print "Job: %15s | JobType: %10s | Arrive Time: %15s | Status: %10s | Elapsed time: %10f " %(jobMetric[0].jobConfig[JOB_NAME], jobMetric[1], time.ctime(jobMetric[2]), jobMetric[3], jobMetric[0].elapsedTime)
       
        if (self.cnt != 0):
            print "Avg job running time of finished jobs is: %f" %(self.totalTime / self.cnt)
        
        if (MONITOR_ON):
            mlog = open(MONITOR_LOG_FILE, 'r')
            totalMu = 0.0
            totalCu = 0.0
            cnt = 0
            for line in mlog:
                data = line.split()
                totalMu += float(data[1])
                totalCu += float(data[2])
                cnt += 1
                
            mlog.close()

            avgMu = 0.0
            avgCu = 0.0
            if (cnt != 0):
                avgMu = totalMu/cnt
                avgCu = totalCu/cnt
            
            print "Cluster usage: "
            print "Average memory usage [%10f%%] "%(avgMu*100)
            print "Average cpu usage [%10f%%] "%(avgCu*100)

