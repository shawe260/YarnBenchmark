#!/usr/bin/python
import os
PWD = os.getcwd()
CONF_DIR = PWD + '/conf/'
TRACE_DIR = 'trace/'
LOG_DIR = 'log/'

'''Job Configure'''
JOB_NAME = "job.name"
JOB_JAR_NAME = "job.jar"
JOB_APP_CLASS = "job.app.class"
JOB_COMMAND = "job.command"
JOB_AM_MEM = "job.am.mem"
JOB_CONTAINERS = "job.container.num"
JOB_CONTAINER_MEM = "job.container.mem"
JOB_CONTAINER_CORES = "job.container.cores"
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

#SPARK job
SPARK_HOME = "/groups/ClusterSched/advcc19/spark-1.0.2-bin-hadoop2"

# Both for mpi and openmp jobs
CONTAINER_MEMORY = 1024
TIMEOUT = 1200

'''Single App Executor'''
SE_RUN_TIMES = 1

'''Random Executor'''
RE_GENERATE_TRACE_ON = True
RE_TARGET_TRACE_FILE = TRACE_DIR + 'randomGenerated.trace'
RE_GEN_DURATION = 300 # The duration that the executor keeps generating jobs
RE_GEN_RAND_LOW = 10 # The lower bound of the random job generation time
RE_GEN_RAND_HIGH = 30 # The upper bound of the random job generation time
RE_BLACK_LIST = {"MapReduce":["randomwriter", "terasort"], "Spark":["sparktest"]} #The application name that will not be randomly generated

'''Trace Executor'''
TRACE_FILE = TRACE_DIR + 'default.trace' 

'''Log'''
LOG_FILENAME = LOG_DIR + 'execution.log'

'''Monitor'''
MONITOR_ON = True
NODE_MONITOR_PERIOD = 5
MONITOR_LOG_PERIOD = 10
MONITOR_LOG_FILE = LOG_DIR + 'monitor.log'
