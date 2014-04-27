import requests
import json
import pprint

# r = requests.get('http://us.battle.net/api/wow/item/18803')
# rj = r.json()
# # print rj

# for key, value in rj.items():
# 	# for key, value in rj.items():
# 		# print "%s : %s" % (key, value)
# 	print "%s -- %s \n" % (key, value)

# print r.text

locales = {'uslocales' : ['en_US', 'es_MX', 'pt_BR'],
		'eulocales' : ['en_GB', 'es_ES', 'fr_FR', 'ru_RU', 'de_DE', 'pt_PT', 'it_IT'],
		# 'krlocale' : ['kr_KR'],
		# 'twlocale' : ['zh_TW'],
		# 'cnlocale' : ['zh_CN']
		}

names = []

for locale in locales.keys():
	for lang in locales[locale]:
		if locale == 'uslocales':
			host = 'us.battle.net'
		elif locale == 'eulocales':
			host = 'eu.battle.net'
		elif locale == 'krlocale':
			host = 'kr.battle.net'
		elif locale == 'twlocale':
			host = 'tw.battle.net'
		elif locale == 'cnlocale':
			host = 'www.battlenet.com.cn'
		r = requests.get('http://%s/api/wow/item/18803?locale=%s' % (host, lang))
		print "Testing locale %s" % lang
		names.append(r.json()['name'])
for name in names:
	print name

# for locale in locales.keys():
# 	for lang in locales[locale]:
# 		if locale == 'uslocales':
# 			r = requests.get('http://us.battle.net/api/wow/item/18803?locale=%s' % lang)
# 			print r.url
# 		elif locale == 'eulocales':
# 			r = requests.get('http://eu.battle.net/api/wow/item/18803?locale=%s' % lang)
# 			print r.url
# 		elif locale == 'krlocale':
# 			r = requests.get('http://kr.battle.net/api/wow/item/18803?locale=%s' % lang)
# 			print r.url
# 		elif locale == 'twlocale':
# 			r = requests.get('http://tw.battle.net/api/wow/item/18803?locale=%s' % lang)
# 			print r.url
# 		elif locale == 'cnlocale':
# 			r = requests.get('http://eu.battle.net/api/wow/item/18803?locale=%s' % lang)
# 			print r.url 
		