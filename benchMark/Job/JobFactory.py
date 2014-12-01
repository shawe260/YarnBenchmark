#!/usr/bin/python

from MapReduceJob import MapReduceJob
from SparkJob import SparkJob
from MPIJob import MPIJob
from OpenMPJob import OpenMPJob

class JobFactory:
    def __init__(self):
        pass

    def __createJob__(self, jobType, config):
        job = {
            'MapReduce': MapReduceJob(config),
            'MPI': MPIJob(config),
            'OpenMP': OpenMPJob(config),
            'Spark': SparkJob(config)
        }.get(jobType, "Not correct")
        # Here should throw execption if the job type does not exist
        return job

if __name__ == "__main__":
    m = JobFactory().__createJob__('MapReduce')
    m.start()
