#!/usr/bin/env python3

import json
import locale
import sys
import reports
import emails
import datetime

print("start!")
def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data



def process_data(data):


  summary = [
    "The {} generated the most revenue: ${} ".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(
         format_car(max_sales_car ), max_sales),
    "The most popular year was {} with {} sales.".format(
         maxyear, maxcountinyear),
  ]
  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data

data = load_data("cars.json")
summary = process_data(data)
lines=''
for line in summary:
    print(type(line))
    print(line)
    line += line+'\n'
print(line)

def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("xxx")
  summary = process_data(data)
  print(summary)
  for line in summary:
    print(type(line))
    #line += line + '\n'
  #print(line)

  # TODO: turn this into a PDF report use: reports.generate() -> '/tmp/cars.pdf'
  reportlist = cars_dict_to_table(data)
  reports.generate("/tmp/cars.pdf","Sales summary for last month",lines.replace("\n","<br/>"),reportlist)

  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "<user>@example.com".format(os.environ.get('USER'))
  subject = "Sales summary for last month"
  body = lines
  message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
  emails.send(message)

  print("ended")
  ###As optional challenges, you could try some of the following functionalities:
  # Sort the list of cars in the PDF by total sales.
  # Create a pie chart for the total sales of each car made.
  # Create a bar chart showing total sales for the top 10 best selling vehicles using the ReportLab Diagra library. Put the vehicle name on the X-axis and total revenue (remember, price * total sales!) along the Y-axis.
