#! /usr/bin/python

from defaults import *

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
            print "Job: %15s | JobType: %10s | Arrive Time: %10f | Status: %10s | Elapsed time: %10f " %(jobMetric[0].jobConfig[JOB_NAME], jobMetric[1], jobMetric[2], jobMetric[3], jobMetric[0].elapsedTime)
       
        if (self.cnt != 0):
            print "Avg job running time of finished jobs is: %f" %(self.totalTime / self.cnt)
