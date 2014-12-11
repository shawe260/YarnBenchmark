
import logging
from Job import Job
from defaults import *


class MPIJob(Job):

    def __init__(self, config):
        super(MPIJob, self).__init__(config)

    def run(self):
        logging.debug("Starting a MPI Job: " + self.jobConfig[JOB_NAME])
        super(MPIJob, self).run()
        logging.debug("MPI job: " + self.jobConfig[JOB_NAME] + " completed")

    def generateYarnCommand(self):
        timeout = TIMEOUT
        cmd = "yarn" \
        + " jar %s/%s org.apache.hadoop.yarn.applications.mpirunner.Client" %(MPI_JOB_POOL_DIR, MPI_RUNNER_JAR)\
        + " --jar %s/%s " %(MPI_JOB_POOL_DIR, MPI_RUNNER_JAR) \
        + " --master_memory 64"        \
        + " --shell_command %s/%s " %(MPI_JOB_POOL_DIR, self.jobConfig[JOB_COMMAND])  \
        + " --num_containers %d " %self.jobConfig[JOB_CONTAINERS]   \
        + " --container_memory %s " %CONTAINER_MEMORY \
        + " --timeout %d" %(timeout * 1000) 
        return cmd
    #container number actually should be in the trace file
