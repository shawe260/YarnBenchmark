#!/usr/bin/python
import time
import os
import sys
import argparse
import logging
from defaults import *
from Executor.ExecutorFactory import ExecutorFactory

logging.basicConfig(filename = LOG_FILENAME,
        level = logging.DEBUG,
        filemode = 'w',
        format = "[%(levelname)s]: %(message)s   {%(threadName)s %(module)s}" ,
        )

def startParser():
    parser = argparse.ArgumentParser(description = "This script is for benchmarking heterogenous jobs on Yarn. See more configuration in directory ./conf")
    parser.add_argument('-e', '--executor', action = 'store', dest = 'executorType', default = 'Trace', help = "Executor Type: [Random, Trace] Default: Trace")
    parser.add_argument('-t', '--timeout', action = 'store', dest = 'timeout', default = TIMEOUT, type = float, help = "Timeout: Default %d"%TIMEOUT)
    results = parser.parse_args()
    return results.executorType, results.timeout


if __name__ == "__main__":
    
    '''
    HADOOP_HOME = os.getenv("HADOOP_HOME")
    
    assert(HADOOP_HOME)
    if HADOOP_HOME not in sys.path:
        sys.path.append(HADOOP_HOME + '/bin')
    '''

    executorType, timeout = startParser()
    executor = ExecutorFactory().__getExecutor__(executorType, timeout)
    executor.__run__()
    executor.__cleanUp__()
    executor.__reportMetrics__()

    print "Benchmarking finished"
