#!/usr/bin/python

from RandomExecutor import RandomExecutor 

class ExecutorFactory():
    executorType = 'Random' 
    # better use a enum.. this is just to test

    def __init__(self, executorType = 'Random'):
        self.executorType = executorType

    def __getExecutor__(self):
        print "Creating a type \"" + self.executorType + "\" executor"
        return {
            'Random' : RandomExecutor(),
        }.get(self.executorType, "Not Correct")
        
if __name__ == "__main__":
    e = ExecutorFactory().__getExecutor__()
    e.__run__()
