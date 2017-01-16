#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import slackweb
import re

host = 'localhost'
port = 10500

# connect julius
clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect((host, port))

sf = clientsock.makefile('rb')

while True:
    line = sf.readline().decode('utf-8')
    if line.find('WHYPO') != -1:
        print line
        if line.find(u'gomi') == -1 and line.find('<sp>') == -1:
            print("webhook-slack")
            cm = re.sub(r'.*CM="([^"]*)".*', r'\1', line)
            if float(cm) > 0.9:
              slack = slackweb.Slack(url="https://hooks.slack.com/services/xxxxxxxxxxxxxxxxxx")
              word = re.sub(r'.*WORD="([^"]*)".*', r'\1', line)
              slack.notify(text=word)
