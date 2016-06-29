#!/usr/bin/python

""" Distributed ICMP ping  """

__author__ = "Marcin Kozlowski <marcinguy@gmail.com>"

from ping_module import isUp

from redis import Redis

from rq import Queue

import os
import argparse

import pprint
import time
import random



if __name__ == '__main__':

    if os.geteuid() != 0:
      exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

    parser = argparse.ArgumentParser(description='Ping Scanner v0.99')
    parser.add_argument('-i','--input', help='Input list of IPs', required=True)
    parser.add_argument('-o','--output', help='Output', required=True)
    parser.add_argument('-s','--shuffle', help='Shuffle', required=True)
    args = parser.parse_args()
    input = args.input
    output = args.output
    shuffle = args.shuffle
    if(shuffle == "yes"):
      with open(input,'rU') as f:
        lines = f.read().splitlines()
      random.shuffle(lines)
      data = lines
    else:
      with open(input,'rU') as f:
         lines = f.read().splitlines()
      data = lines

    results_list = list()
    q = Queue(connection=Redis(host='localhost', port=6379))
    for ip in data:
        results_list.append(q.enqueue(isUp, ip))
    #pprint.pprint(results)
    resfile = open(output,'w')
    for ret in results_list:
        while(ret.status!="finished"):
            time.sleep(0.01)
        resfile.write(ret.return_value+"\n")





