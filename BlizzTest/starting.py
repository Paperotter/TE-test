import requests
import json
from pprint import pprint

## Basic GET request and Invalid endpoint Negative test ##

#Test results bools
statusTest = False
reasonTest = False
authTest = False
miscFail = False

#Unexpected List
Unexpecteds = []

#Results Log
testResults = open('resultslog.txt', 'w')


#Perform basic GET request to ensure fail tests are legitimate, and then carry on with Fail case testing
tests = ['18803', 'fail']

for entry in tests:
	r = requests.get('http://us.battle.net/api/wow/item/%s' % entry)
	data = r.json()

	print "Getting json for the following endpoint:"
	print r.url + '\n'

	if entry == 'fail':
		for key in data:
			if key == 'status':
				returnedStatus = "%s -- %s" % (key, data[key])
				print 'STORING \n%s' % returnedStatus
			elif key == 'reason':
				returnedReason = "%s -- %s" % (key, data[key])
				print 'STORING \n%s' % returnedReason
			else:
				with open('%s.json' % entry, 'w') as output:
					json.dump(data, output, sort_keys=True,
	 				indent=4, separators=(',', ': '))
				failFail = "Unexpected data found in json - Logged in json id"
				print failFail
				Unexpecteds.append(failFail)
				miscFail = True
		
		if returnedStatus == "status -- nok":
			statusTest = True
			print "Failed request returned status correctly"
		else:
			print "Failed request error is fail"

		if returnedReason == "reason -- When in doubt, blow it up. (page not found)":
			reasonTest = True
			print "Failed request returned reason correctly"
		else:
			print "Failed request error is fail"

	else:
		for key in data:
			if key == 'name':
				print "Legitimate data found for '%s'. \nMove along..." % data[key]
			else:
				with open('%s.json' % entry, 'w') as output:
					json.dump(data, output, sort_keys=True,
	 				indent=4, separators=(',', ': '))
	 			miscFail = True
				badGet = "This isn't the item id you were looking for... or worse. \nJSON data exported to a file for verification."
				Unexpecteds.append(badGet)
				print badGet



## Authentication Test ##
# print "\n## Authentication Test ##\n"
# r = requests.get('http://us.battle.net/api/wow/item/18803', auth=('test', 'testpass'))
# print "Getting json for the following endpoint (with tacked on authentication):"
# print r.url + '\n'
# data = r.json()

# dump = json.dumps(r.json(), indent=4, separators=(',', ': '))
# dump = json.dumps(data, sort_keys=True,
# 	 				indent=4, separators=(',', ': '))
# print dump

## Localization Tests ##


## Log Results ##
testResults.write("Fail test Results (True = Pass, False = Fail):\n")
testResults.write("Failed status test: %r\n" % statusTest)
testResults.write("Failed reason test: %r\n" % reasonTest)
testResults.write("Failed authentication test: %r\n" % authTest)
testResults.write("\n#####\n")
if not Unexpecteds:
	testResults.write("No Unexpected Errors")
else: 
	testResults.write("Unexpected Errors log:\n")
	for log in Unexpecteds:
		testResults.write('%s\n' % log)