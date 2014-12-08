#!/usr/bin/python
import os
PWD = os.getcwd()
CONF_DIR = PWD + '/conf/'
TRACE_DIR = 'trace/'

'''Job Configure'''
JOB_NAME = "job.name"
JOB_JAR_NAME = "job.jar"
JOB_COMMAND = "job.command"
JOB_CONTAINERS = "job.containers.num"
JOB_TYPES = ['MapReduce', 'MPI', 'OpenMP', 'Spark'] # a list of job types, 0: MapReduce, 1: MPI ...
JOB_CONF_FILE = CONF_DIR + 'jobconfig.json'
JOB_POOL_DIR = PWD + '/jobpool/'

#MPI Job
MPI_JOB_POOL_DIR = JOB_POOL_DIR
MPI_RUNNER_JAR = "hadoop-yarn-applications-mpirunner-2.2.0.jar"

#OPENMP Job 
OPENMP_JOB_POOL_DIR = JOB_POOL_DIR
OPENMP_RUNNER_JAR = "hadoop-yarn-applications-gpu-2.2.0.jar"
OPENMP_NUM_CORES_BIG = 4
OPENMP_NUM_CORES_SMALL = 2

# Both for mpi and openmp jobs
CONTAINER_MEMORY = 1024
TIMEOUT = 1200000

'''Single App Executor'''
SINGLE_EXECUTOR_CONF_FILE = CONF_DIR + 'singleAppExecutor.json'

'''Random Executor'''
RAND_EXECUTOR_CONF_FILE = CONF_DIR + 'randExecutor.json'
generateTrace = True
TARGET_TRACE_FILE = TRACE_DIR + 'randomGenerated.trace'

'''Trace Executor'''
TRACE_EXECUTOR_CONF_FILE = CONF_DIR + 'traceExecutor.json'
#Default Trace
TRACE_FILE = TRACE_DIR + 'test.trace'

'''Log'''
LOG_FILENAME = 'execution.log'

'''Monitor'''
MONITOR_ON = True
NODE_MONITOR_PERIOD = 10
MONITOR_LOG_PERIOD = 15
MONITOR_LOG_FILE = 'monitor.log'
