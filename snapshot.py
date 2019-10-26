#!/usr/bin/env python
import time
from time import gmtime, strftime
import psutil
import json


class CompInfo:

    def __init__(self):
        self.mb = 1024 * 1024
        self.cpu = psutil.cpu_percent()
        self.mem = psutil.disk_usage('/').used
        self.vmem = psutil.virtual_memory().active
        self.iodiskr = psutil.disk_io_counters().read_bytes
        self.iodiskw = psutil.disk_io_counters().write_bytes
        self.ionets = psutil.net_io_counters().packets_sent
        self.ionetr = psutil.net_io_counters().packets_recv

    def cpuload(self):
        return self.cpu

    def memus(self):
        return self.mem // self.mb

    def vmemus(self):
        return self.vmem // self.mb

    def iodiskbytes(self):
        return str(self.iodiskr // self.mb), str(self.iodiskw // self.mb)

    def ionetpack(self):
        return self.ionets, self.ionetr


def WriteToJson(file, timer):

    i = 0
    data = {}
    while True:

        cinfo = CompInfo()

        data['SNAPSHOT ' + str(i + 1) + ": " + strftime("%Y-%m-%d %H:%M:%S", gmtime())] = {
            "Cpu Load": str(cinfo.cpuload()) + "%",
            "Memory usage": str(cinfo.memus()) + "mb",
            "Virtual Memory Usage": str(cinfo.vmemus()) + "mb",
            "I/O disk": "Read: " + "mb/Write: ".join(cinfo.iodiskbytes()) + "mb",
            "I/O network, packets": "Sent: " + "/Received: ".join(cinfo.iodiskbytes())}

        with open(file, 'w') as outfile:
            json.dump(data, outfile, indent=3)

        i += 1
        time.sleep(timer * 60)


def WriteToFile(file, timer):

    fileTxt = open(file, "w+")
    i = 0
    while True:
        fileTxt = open(file, "a+")
        cinfo = CompInfo()
        fileTxt.write('SNAPSHOT ' + str(i + 1) + ": "
                      + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ":\r\n")
        fileTxt.write("\t\t\t Cpu Load: %s\r\n" % str(cinfo.cpuload()))
        fileTxt.write("\t\t\t Memory usage: %s mb\r\n " % str(cinfo.memus()))
        fileTxt.write("\t\t\t Virtual memory usage: %s mb\r\n" % str(cinfo.vmemus()))
        fileTxt.write("\t\t\t I/O disk. Read: %s mb Write: %s mb\r\n" % cinfo.iodiskbytes())
        fileTxt.write("\t\t\t I/O network, packets. Read %s Write: %s\r\n" % cinfo.iodiskbytes())
        fileTxt.close()
        i += 1
        time.sleep(timer * 60)
