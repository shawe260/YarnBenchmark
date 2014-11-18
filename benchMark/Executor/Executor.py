#!/usr/bin/python
'''An abstract class definition for a job executor'''


class Executor:
# should also have machenism for receving metrics
    def __init__(self):
        pass

    def __run__(self):
        raise NotImplementedError

    def __getNextJob(self):
        raise NotImplementedError
