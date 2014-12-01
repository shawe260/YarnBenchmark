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
    executorConfig = {}
    runningJobMap = {} 
    jobType = JOB_TYPES
    collector = MetricsCollector()
    
    def __init__(self, executor_config_file, timeout):
        self.__loadJobPool()
        self.__loadExecutorConfig(executor_config_file)
        logging.debug("Spawning a thread to kill the applications that timeout, the timeout is %d" %timeout)
        t = threading.Thread(name = 'TimeoutThread',
                target = self.startTimeout,
                args = (timeout,)
                )
        # set it up as a daemon thread so that it will only exit when the program is running, and will automatically terminate when the program is done
        t.setDaemon(True)
        t.start()

    def __cleanUp__(self):
        for (job, jobType, arrt), status in self.runningJobMap.iteritems():
            self.collector.reportJobFinish(job, jobType, arrt, status)

    def __reportMetrics__(self):
        self.collector.generateReport()

    def __run__(self):
        raise NotImplementedError

    def __getNextJob(self):
        raise NotImplementedError
    
    def __loadJobPool(self): 
        jobPoolFd = open(JOB_CONF_FILE, 'r') # TODO: make it to per worload configuration file, now all the jobs are put in one file
        self.jobPool = json.load(jobPoolFd)
        jobPoolFd.close()

    def __loadExecutorConfig(self, executor_config_file):
        reConfigFd = open(executor_config_file, 'r')
        self.executorConfig = json.load(reConfigFd) 
        reConfigFd.close()
    
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
