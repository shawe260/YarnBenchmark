#!/usr/bin/python

import time
from Executor.ExecutorFactory import ExecutorFactory


if __name__ == "__main__":
    print "Start Benchmarking..."
    # Todo "Usage: ....."
    # Add command line parser in this to parse the and get different exection mod 
    executor = ExecutorFactory().__getExecutor__('Random') # Should I add ending criteria?
    executor.__run__()
    time.sleep(5)
    print "Reporting the metrics"
    print "2 applications finished...generating report"
    print "No report avaiable right now"
    time.sleep(5)
    print "BenchMark finished"
