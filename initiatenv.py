#!/usr/bin/env python

# Authenticate API
# Call POST Rest API endpoint
# Pass response to the variable

#Step 1 - import the required libraries


#########################################################################################
#########################################################################################
########################## Modify The Section Below  ####################################
username ='582e86d4-d0f6-4feb-9da9-7a585027e488'
password ='SL2srkeC5GZR7vScd12qlOGgg743XmNM'
callbackUrl ='https://requestb.in/1b00wx01' 
successUrl = 'https://requestb.in/1b00wx01'
errorUrl = 'https://requestb.in/1b00wx01'


def  post_to_initiateNetverify (successUrl, errorUrl, username, password, callbackUrl):
	headers = {
		'Accept':'application/json',
		'Content-Type':'application/json',
		'User-Agent':'JumioInc Linda/1.0.0'
	}
	data = {
		'merchantIdScanReference':'lindamerchantid',
		'successUrl':successUrl,
		'errorUrl':errorUrl,
		'callbackUrl':callbackUrl
	}

	url =  'https://netverify.com/api/netverify/v2/initiateNetverify'
	r = requests.post(url=url, data=json.dump(data), headers=headers, auth=HTTPBasicAuth(username, password))
	return r.text

post_to_initiateNetverify (successUrl, errorUrl, username, password, callbackUrl)