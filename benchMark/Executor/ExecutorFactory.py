#!/usr/bin/python

from Executor import Executor
from TraceExecutor import TraceExecutor
from RandomExecutor import RandomExecutor 

class ExecutorFactory():
    def __init__(self):
        pass

    def __getExecutor__(self, executorType, timeout):
        executor = {
            'Random' : RandomExecutor(timeout),
            'Trace' : TraceExecutor(timeout)
        }.get(executorType, "Not Correct")
        assert isinstance(executor, Executor), '%s is not a supported executorType'%executorType 
        print "Starting a \"" + executorType + "\" Executor"
        return executor
        
if __name__ == "__main__":
    e = ExecutorFactory().__getExecutor__()
    e.__run__()
