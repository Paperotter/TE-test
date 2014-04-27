import requests
import json
from pprint import pprint

## Basic GET request and Invalid endpoint Negative test ##

tests = ['18803', 'fail']

for entry in tests:
	r = requests.get('https://us.battle.net/api/wow/item/%s' % entry)
	rjson = r.json()

	print "Generating json for the following endpoint:"
	print r.url + '\n'

	with open("%s.json" % entry, "w") as output:
	 	json.dump(rjson, output, sort_keys=True,
					indent=4, separators=(',', ': '))

## Localization Tests ##

locales = {'uslocales' : ['en_US', 'es_MX', 'pt_BR'],
		'eulocales' : ['en_GB', 'es_ES', 'fr_FR', 'ru_RU', 'de_DE', 'pt_PT', 'it_IT'],
		'krlocale' : 'kr_KR'}

for locale in locales.keys():
	for lang in locale.values():
		if locale == 'uslocales':
			r = requests.get('https://us.battle.net/api/wow/item/18803?locale=%s' % lang)
