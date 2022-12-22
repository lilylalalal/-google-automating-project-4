#! /usr/bin/env python3
import os
import requests
import json

def reading(directory,f):
    coms =[]
    img = f.replace('.txt','.jpeg')
    txtfile = open(directory+f ,"r")
    txtfile = txtfile.readlines()
    for lines in txtfile:
        lines = lines.rstrip()
        #print(lines) # type:str
        coms.append(lines)

    data = coms
    data[1] = coms[1].strip(" lbs")
    data.append(img)
    #print(data)
    return data


def makedict(com):
    heading = ["name", "weight", "description","image_name"]
    commentdict = {}
    commentdict = {heading : com for heading, com in zip(heading, com)}
    #print(commentdict)
    #add photo into dict

    return commentdict

def readuploadfile(directory):
    file = os.listdir(directory)
    #print(file)
    for f in file :
        newf = f.replace('.txt','.json')
        comment = reading(directory,f)
        fruitdict = makedict(comment)
        with open(newf,'w') as f_json:
            json.dump(fruitdict,f_json)
        #response = requests.post("http://localhost/fruits/", data=fruitdict )
        #print(response.status_code)
        print(fruitdict)
    return fruitdict

comments = readuploadfile('descriptions/')
#comments = readuploadfile('supplier-data/descriptions/')
