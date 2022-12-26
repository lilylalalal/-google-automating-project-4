#!/usr/bin/env python3

import json
import locale
import sys,os
import reports
import emails
from datetime import date

def loaddata(directory, filename):
  """1.Loads the contents of filename from txt file
  and then generate name &weight."""
  txtfile = open(directory+filename,'r')
  txtfile = txtfile.readlines()
  weight = txtfile[1]
  name = txtfile[0]

  summary = """
  name: {}
  <br/>
  weight: {}
  <br/>
  """.format(name,weight)
  #print(summary)
  return summary

if __name__ == "__main__":
#Process the txt file and generate a full report out of it.
    today = str(date.today())
    title = "Prpcessed Update on "+ today
    file = os.listdir("supplier-data/descriptions/")
#  turn this into a PDF report use: reports.generate() -> '/tmp/processed.pdf'
    alldata = ''
    for filename in file:
        data = loaddata("supplier-data/descriptions/",filename)
        alldata += data +"<br/>"
    print(alldata)
    reports.generate("/tmp/processed.pdf",title,alldata)
    # send the PDF report as an email attachment
    sender = "automation@example.com"
    receiver = "<user>@example.com".format(os.environ.get('USER'))
    subject = " Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)
