#!/bin/bash
#Start the marmot cluster

if [ "$#" != "2" ]; then
	echo -e "Usage: startImage <NameOfTheExperiment> <Number of nodes>"
	exit 0
fi

/share/probe/bin/probe-makebed -e $1 -p OpenStackSys -i Yarn -n $2 -g Group13
