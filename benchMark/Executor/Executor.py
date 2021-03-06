#!/usr/bin/python
'''base class for a job executor'''

import json
import logging
import threading
import time
import subprocess
from Metrics.MetricsCollector import MetricsCollector
from defaults import *

"""
Executor launches job via user defined behaviour (eg. Trace or Random), and collect metrics from user
"""
class Executor(object):

    jobPool = {}
    runningJobMap = {} 
    jobType = JOB_TYPES
    collector = MetricsCollector()
    
    def __init__(self, timeout):
        self.__loadJobPool()
        self.timeout = timeout
        
    def __cleanUp__(self):
        for (job, jobType, arrt), status in self.runningJobMap.iteritems():
            self.collector.reportJobFinish(job, jobType, arrt, status)

    def __reportMetrics__(self):
        self.collector.generateReport()

    def __run__(self):
        logging.debug("Spawning a thread to kill the applications that timeout, the timeout is %d" %self.timeout)
        t = threading.Thread(name = 'TimeoutThread',
                target = self.startTimeout,
                args = (self.timeout,)
                )
        # set it up as a daemon thread so that it will only exit when the program is running, and will automatically terminate when the program is done
        t.setDaemon(True)
        t.start()
        self.run()
        for runningJob in self.runningJobMap:
            runningJob[0].join()

    def run(self):
        raise NotImplementedError

    def __getNextJob(self):
        raise NotImplementedError
    
    def __loadJobPool(self): 
        jobPoolFd = open(JOB_CONF_FILE, 'r') # TODO: make it to per worload configuration file, now all the jobs are put in one file
        self.jobPool = json.load(jobPoolFd)
        jobPoolFd.close()

    """
    Funtion for a timeout thread, the thread will kill all exisiting application if timeout
    """
    def startTimeout(self, timeout):
        logging.debug("sleeping for %d secs" %timeout)
        time.sleep(timeout) 
        self.killAllApps()
        logging.debug("All the running applications are killed")
    
    def killAllApps(self):
        #setting the running status of the alive Job to be Killed

        ps = subprocess.Popen(('yarn', 'application', '-list'), stdout = subprocess.PIPE)
        output = subprocess.check_output(('egrep', 'application_'), stdin = ps.stdout)
        ps.wait()

        for runningJob in self.runningJobMap.keys():
            if (runningJob[0].elapsedTime == None):
                self.runningJobMap[runningJob] = 'Killed'

        for line in output.split('\n'):
            logging.debug(line)
            linelst = line.strip().split()
            if len(linelst) < 1:
                continue
            appid = linelst[0]
            logging.debug("KILLING application %s"%appid)
            subprocess.call("yarn application -kill %s"%appid, shell = True)
