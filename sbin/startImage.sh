#!/bin/bash
#Start the marmot cluster

if [ "$#" != "2" ]; then
	echo -e "Usage: startImage <NameOfTheExperiment> <Number of nodes>"
	exit 0
fi

/share/probe/bin/probe-makebed -e $1 -p OpenStackSys -i yarn-2 -n $2 -g Group13 -s /users/shiweid/capstone/YarnBenchmark/sbin/startup 
#/share/probe/bin/generic-startup

