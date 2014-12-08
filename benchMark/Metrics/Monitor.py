#! /usr/bin/python

import subprocess
import logging
import threading
import time
from defaults import *

class Monitor():
   
    nodeList = []
    monitorThreadsList = []
    clusterStates = {}
    logThread = None

    def __init__(self):
        output = subprocess.check_output("yarn node -list -all 2>/dev/null | awk 'NR>2{print $1}'", shell = True)
        self.nodeList = output.split()
        self.numNodes = len(self.nodeList)

    def start(self):
        self.running = True
        if self.numNodes != 0:
            print 'There are %d nodes in the cluster' %self.numNodes
            self.startMonitoringThreads()

    def end(self):
        self.running = False
        for mt in self.monitorThreadsList:
            mt.join()

        if (self.logThread):
            self.logThread.join()

    def startMonitoringThreads(self):
        self.logThread = threading.Thread(name = 'monitorLogging', target = self.logging)
        self.logThread.setDaemon(True)
        self.logThread.start()

        for t in range(0, self.numNodes):
            mt = threading.Thread(name = 'NODE_%d'%t , target = self.monitorNode, args = (self.nodeList[t],))
            mt.setDaemon(True)
            mt.start()
            self.monitorThreadsList.append(mt)
                
    def logging(self):
        #buff size is zero, so flush to disk as soon as written
        log = open(MONITOR_LOG_FILE,'w', 0);
        curTime = 0
        while(self.running):
            logging.debug('Current cluster state :')
            logging.debug('Total nodes: %d'%len(self.clusterStates))
            logging.debug('TotalRunningContainers : %d'%self.getNumContainers())
            tum = self.getTotalUsedMemory()
            tam = self.getTotalAvailableMemory()
            if (tam == 0):
                mu = 0
            else:
                mu = float(tum)/tam
            logging.debug('Total memory used : %d, Total memory available: %d, Usage: %f'%(tum,tam,mu))
            tuc = self.getTotalUsedVcpus()
            tac = self.getTotalAvailableVcpus()
            if (tac == 0):
                cu = 0
            else:
                cu = float(tuc)/tac
            logging.debug('Total vcpu used : %d, Total vcpu available: %d, Usage: %f'%(tuc,tac,cu))
            log.write("%d %10f %10f\n"%(curTime, mu, cu))
            curTime += MONITOR_LOG_PERIOD
            time.sleep(MONITOR_LOG_PERIOD)
        log.close()

    def getNumContainers(self):
        res = 0
        for k, r in self.clusterStates.iteritems():
            res += r[0]
        return res

    def getTotalUsedMemory(self):
        res = 0
        for k, r in self.clusterStates.iteritems():
            res += r[1]
        return res


    def getTotalAvailableMemory(self):
        res = 0
        for k, r in self.clusterStates.iteritems():
            res += r[2]
        return res

    def getTotalUsedVcpus(self):
        res = 0
        for k, r in self.clusterStates.iteritems():
            res += r[3]
        return res


    def getTotalAvailableVcpus(self):
        res = 0
        for k, r in self.clusterStates.iteritems():
            res += r[4]
        return res

    def monitorNode(self, node):
        while (self.running):
            output = subprocess.check_output("yarn node -status %s 2>/dev/null"%node, shell = True)
            # only need the containers, memory used, memory capacity, cpu used, cpu capcity
            result = output.split('\n')[7:-2]
            containers = int(result[0].split(' : ')[1])
            memoryUsed = int(result[1].split(' : ')[1][:-2])
            memoryCapacity = int(result[2].split(' : ')[1][: -2])
            vcpuUsed = int(result[3].split(' : ')[1][: -7])
            vcpuCapacity = int(result[4].split(' : ')[1][: -7])
            record = (containers, memoryUsed, memoryCapacity, vcpuUsed, vcpuCapacity)
            self.clusterStates[node] = record
            time.sleep(NODE_MONITOR_PERIOD);
