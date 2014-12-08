#!/usr/bin/python
import time
import os
import sys
import argparse
import logging
import Executor.ExecutorFactory as ef
from Metrics.Monitor import Monitor
from defaults import *

logging.basicConfig(filename = LOG_FILENAME,
        level = logging.DEBUG,
        filemode = 'w',
        format = "[%(levelname)s]: %(message)s   {%(threadName)s %(module)s}" ,
        )

def startParser():
    parser = argparse.ArgumentParser(description = "This script is for benchmarking heterogenous jobs on Yarn. See more configuration in directory ./conf")
    parser.add_argument('-e', '--executor', action = 'store', dest = 'executorType', default = 'Trace', help = "Executor Type: [Random, Trace, Single] Default: Trace")
    parser.add_argument('-t', '--timeout', action = 'store', dest = 'timeout', default = TIMEOUT, type = float, help = "Timeout in seconds: Default %d"%TIMEOUT)
    parser.add_argument('-jt', '--jobtype', action = 'store', dest = 'jobType', help = "Only used for SingleAppExecutor, specify a jobtype [0:MapReduce, 1:MPI, 2:OpenMP, 3:Spark]", type = int)
    parser.add_argument('-jn', '--jobname', action = 'store', dest = 'jobName', help = "Only used for SingelAppExecutor, specify the jobname")
    parser.add_argument('-tr', '--trace', action = 'store', dest = 'traceFile', help = "Only used for TraceExecutor. Default trace file (in /conf) will be used, if not specified ")
    results = parser.parse_args()
    return results


if __name__ == "__main__":
    
    '''
    HADOOP_HOME = os.getenv("HADOOP_HOME")
    
    assert(HADOOP_HOME)
    if HADOOP_HOME not in sys.path:
        sys.path.append(HADOOP_HOME + '/bin')
    '''

    results = startParser()

    monitor = Monitor()
    monitor.start()

    starter = ef.ExecutorStarter(results.timeout, results.executorType, results.jobType, results.jobName, results.traceFile)
    executor = ef.ExecutorFactory().__getExecutor__(starter)
    executor.__run__()
    executor.__cleanUp__()
    executor.__reportMetrics__()

    monitor.end()

    print "Benchmarking finished"
