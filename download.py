#!/usr/bin/env python3
import os
import sys
import http.server
import subprocess
import json

#script to download sample cases.

def listen(*, timeout=None):
    json_data = None
    class CompetitiveCompanionHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            nonlocal json_data
            json_data = json.load(self.rfile)

    with http.server.HTTPServer(('127.0.0.1', 10046), CompetitiveCompanionHandler) as server:
        server.timeout = timeout
        server.handle_request()
    if json_data is None:
        print("failed")
    print(json_data)
    return json_data

def create_tests():
    prob = listen()
    #prob is a dictionary containing all of json data
    if prob is None:
        return
    cnt = 1
    for test in prob["tests"]:
        #create a .in and .out file
        name = "Sample" + str(cnt)
        #create new files and write the required cases to there.
        os.system("touch " + name + ".in")
        os.system("touch " + name + ".out")

        with open(name + ".in", "w") as inp:
            inp.write(test["input"])

        with open(name + ".out", "w") as op:
            op.write(test["output"])

        cnt += 1

create_tests()
