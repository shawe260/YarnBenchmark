#!/usr/bin/python

from Executor import Executor
from TraceExecutor import TraceExecutor
from RandomExecutor import RandomExecutor 
from SingleAppExecutor import SingleAppExecutor

class ExecutorStarter():
    timeout = 0
    executorType = ''
    jobType = 0
    jobName = ''
    traceFile = ''

    def __init__(self, timeout, et, jt, jn, tf):
        self.timeout = timeout
        self.executorType = et
        self.jobType = jt
        self.jobName = jn
        self.traceFile = tf

class ExecutorFactory():
    def __init__(self):
        pass

    def __getExecutor__(self, starter):
        executor = {
            'Random' : RandomExecutor(starter.timeout),
            'Trace' : TraceExecutor(starter.traceFile, starter.timeout),
            'Single' : SingleAppExecutor(starter.jobType, starter.jobName, starter.timeout), 
        }.get(starter.executorType, "Not Correct")
        assert isinstance(executor, Executor), '%s is not a supported executorType'%executorType 
        print "Starting a \"" + starter.executorType + "\" Executor"
        return executor
        
if __name__ == "__main__":
    e = ExecutorFactory().__getExecutor__()
    e.__run__()
