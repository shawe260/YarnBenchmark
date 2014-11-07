#!/usr/bin/python

import subprocess


print "This script is used to benchmark"

print "Start an MR program"
#/usr/local/Hadoop2.0/hadoop-2.4.1/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.4.1.jar
DIR = "/usr/local/Hadoop2.0/hadoop-2.4.1/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.4.1.jar"
s = open("lolo1.txt", "w")

subprocess.Popen(["yarn", "jar", DIR, "randomwriter", "out8"], stdout = s, stderr = s);

print "I am here, not blocked lol"
