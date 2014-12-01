#!/usr/bin/python
import os
PWD = os.getcwd()
'''The default variables for the benchmark scripts'''
CONF_DIR = PWD + '/conf/'
PWD = "/groups/ClusterSched/advcc19/719/benchMark/"

# Job Configure
JOB_NAME = "job.name"
JOB_JAR_NAME = "job.jar"
JOB_COMMAND = "job.command"
JOB_CONTAINERS = "job.containers.num"
JOB_TYPES = ['MapReduce', 'MPI', 'OpenMP', 'Spark'] # a list of job types, 0: MapReduce, 1: MPI ...
JOB_CONF_FILE = CONF_DIR + 'jobconfig.json'
JOB_POOL_DIR = PWD + '/jobpool/'

# jar should be put under job_pool
MPI_JOB_POOL_DIR = JOB_POOL_DIR
MPI_RUNNER_JAR = "hadoop-yarn-applications-mpirunner-2.2.0.jar"

OPENMP_JOB_POOL_DIR = JOB_POOL_DIR
OPENMP_RUNNER_JAR = "hadoop-yarn-applications-gpu-2.2.0.jar"
OPENMP_NUM_CORES_BIG = 4
OPENMP_NUM_CORES_SMALL = 2

# Defaults
CONTAINER_MEMORY = 7128
TIMEOUT = 1200000

#About executor

#Random Executor
RAND_EXECUTOR_CONF_FILE = CONF_DIR + 'randExecutor.json'

#Trace Executor
TRACE_EXECUTOR_CONF_FILE = CONF_DIR + 'traceExecutor.json'

#Trace
TRACE_DIR = CONF_DIR
TRACE_FILE = TRACE_DIR + 'testtrace'

#Log
LOG_FILENAME = 'testlog.log'

