#!/usr/bin/env python

#########################################################################################
#########################################################################################
########################## Modify The Section Below  ####################################
username ='582e86d4-d0f6-4feb-9da9-7a585027e488'
password ='SL2srkeC5GZR7vScd12qlOGgg743XmNM'
callbackUrl ='https://requestb.in/17z0te31' #Define an endpoint in your API Server. You 
# could also use requestbin.in to see a sample callback
#########################################################################################
#########################################################################################
##########################################################################################
#### DO NOT CHANGE ##### DO NOT CHANGE #### DO NOT CHANGE #### DO NOT CHANGE #############

import os                                   ## Required to read files from OS
import json                                 ## Required to jsonify text
import ssl                                  ## Needed for SSL
import requests                             ## Required to issue API calls
from requests.auth import HTTPBasicAuth     ## Basic authentication on the API calls
import base64                               # Requred to encode images to base 64
from requests.packages.urllib3.exceptions import InsecureRequestWarning #Suppress insecure warnings about adding certificate verification

path="./PHOTO/"

##########################################################################################
### Get list of files in the our photos directory
def get_list_of_files(path):
    return os.listdir(path)


##########################################################################################
### Read the file and return the base64 string
def read_and_encode_func(file_to_read):
    file = open(file_to_read,'rb')
    encoded64=base64.b64encode(file.read())
    return encoded64

##########################################################################################
## Post the encoded image and return the name
def post_encoded_image_func(encoded64, name_of_photo,username,password, callbackUrl):
    # requests.packages.urllib3.disable_warnings()
    headers = {
        'Accept':'application/json',
        'Content-Type':'application/json',
        'User-Agent':'JumioInc Linda/1.0.0'
        }
    data = {
       'merchantIdScanReference':name_of_photo,
       'frontsideImage':encoded64,
       'callbackUrl':callbackUrl,
       'idType':'ID_CARD',
       'country':'USA',
       'enabledFields':'idNumber,idFirstName,idLastName,idDob,idExpiry,idUsState,idPersonalNumber,idAddress'
       }

    url = 'https://netverify.com/api/netverify/v2/performNetverify'

    r = requests.post(url=url, data=json.dumps(data), headers=headers, auth=HTTPBasicAuth(username, password))
    return r.text

list_of_photos=get_list_of_files(path)

##########################################################################################
## Iterates through the files in the photo directory and send it to Netverify
def iterate_files_func(list_of_photos):
    for name_of_photo in list_of_photos:
        enc=read_and_encode_func('./'+path+'/'+name_of_photo)
        print post_encoded_image_func(enc,name_of_photo,username, password, callbackUrl)
    return

##########################################################################################
## Calls the list of photos
iterate_files_func(list_of_photos)
