
import logging
from Job import Job
from defaults import *

class OpenMPJob(Job):

    def __init__(self, config):
        super(OpenMPJob, self).__init__(config)

    def run(self):
        logging.debug("Starting an OpenMP job: " + self.jobConfig[JOB_NAME])
        super(OpenMPJob, self).run()
        logging.debug("OpenMP job: " + self.jobConfig[JOB_NAME] + " completed")

    def generateYarnCommand(self):
        timeout = TIMEOUT 
        cmd = 'yarn' \
        + " jar %s/%s org.apache.hadoop.yarn.applications.gpu.Client " %(OPENMP_JOB_POOL_DIR, OPENMP_RUNNER_JAR) \
        + " --jar %s/%s " %(OPENMP_JOB_POOL_DIR, OPENMP_RUNNER_JAR)       \
        + " --master_memory 64 "                           \
        + " --shell_command 'OMP_NUM_THREADS=%%v\ %s/%s' " %(OPENMP_JOB_POOL_DIR, self.jobConfig[JOB_COMMAND]) \
        + " --num_containers %d" %self.jobConfig[JOB_CONTAINERS]  \
        + " --numCoresBig %s " %OPENMP_NUM_CORES_BIG    \
        + " --numCoresSmall %s " %OPENMP_NUM_CORES_SMALL    \
        + " --container_memory %s" %CONTAINER_MEMORY \
        + " --timeout %d" %(timeout * 1000)
        return cmd
