#!/usr/bin/python3
import sys
import requests
import json
from datetime import datetime
from socket import getfqdn

SLACK_INCOMING_WEBHOOK_URL = "https://hooks.slack.com/services/????????/????????"

user="(null)"
ip="(null)"

if len(sys.argv) >= 3:
  user=sys.argv[1]
  ip=sys.argv[2]

requests.post(SLACK_INCOMING_WEBHOOK_URL, data = json.dumps({
    "attachments":[
       {
           "thumb_url":"https://i.gyazo.com/a4eebbcabc7294ad9599f7aed5d16595.png",
           "fields":[
               {
                   "title":"date",
                   "value":datetime.now().isoformat(),
                   "short":True
               },
               {
                   "title":"host",
                   "value":getfqdn(),
                   "short":True
               },
               {
                   "title":"username",
                   "value":user,
                   "short":True
               },
               {
                   "title":"from",
                   "value":ip,
                   "short":True
               }
           ]
       } 
	]
}))

