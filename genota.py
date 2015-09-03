#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json

BLACKLIST = 'blacklist'
WHITELIST = 'whitelist'
CONTROLVERSION = 2400
PUBLICVERSION = 20
CHANGELOG = 'changelog'

def file2list(filename):
	ret = ''
	with open(filename) as f:
		for line in f:
			ret += line.strip() + ','
	return ret

def file2string(filename):
	with open(filename, 'r') as f:
		return f.read().replace('\n', '')

def main():
	response = {}
	response['controlVersion'] = CONTROLVERSION
	response['publicVersion'] = PUBLICVERSION
	response[BLACKLIST] = file2list(BLACKLIST)
	response[WHITELIST] = file2list(WHITELIST)
	response[CHANGELOG] = file2string(CHANGELOG)
	f = open('index.html', 'w')
	f.write(json.dumps(response, ensure_ascii=False))
	f.close()

if __name__ == '__main__':
	main()